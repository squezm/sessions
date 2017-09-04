from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from msg_board.forms import Msg_boardForm, Board_choice_pollForm, LoginForm, AccountForm
from msg_board.models import Msg_post, Location, Board_choice_poll
from django.views import View
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


class LoginView(View):
    login_form = LoginForm()

    def get(self, request):
        location = request.GET['next'].lstrip('/msg_board/locations/') #get the raw string of the location only
        return render(request, 'msg_board/login.html', {'location': location, 'login_form': self.login_form})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            next = request.GET['next']
            return HttpResponseRedirect(next)                
        else:
            message = "Invalid username or password, please try again."
            print(message)
            return HttpResponseRedirect( reverse('msg_board:error_page', args=(message,)) )


class GuestLoginView(View):
    """View used to login as a guest."""

    def get(self, request, location):
        username = 'guest'; password = 'password1234'
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            return HttpResponse("Guest login functionality is currently disabled. Please try again later.")
        if request.user.is_authenticated:
            print(request.user.username + " is logged in.")
            if location == 'home':
                return HttpResponseRedirect( reverse('msg_board:message_index') )
        else:
            return render(request, 'msg_board/index.html')
        return HttpResponseRedirect( reverse('msg_board:message_board', args=(location,)) )


class CreateAccountView(View):
    account_form = AccountForm()

    def get(self,request):
        return render(request, 'msg_board/create_account.html', {'account_form': self.account_form})

    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        #Need to add validation against the user database here / send the user an email with their info
        user = User.objects.create_user(username, email=email, password=password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            print(user)
        return render(request, 'msg_board/index.html')


class LogoutView(View):

    def get(self, request):
        user = request.user.username
        logout(request)
        if not request.user.is_authenticated:
            print(user + " has logged out.")
        return HttpResponseRedirect( reverse('msg_board:message_index') )


class ErrorView(View):

    def get(self, request, error):
        print(error)
        return render(request, 'msg_board/error.html', {'error_message': error})


class MessageBoardIndexView(View):

    l = Location.objects.all()
    header = 'Post a Session, Read a Session.'
    login_form = LoginForm()
    board_poll_form = Board_choice_pollForm()

    def get(self, request):        
        if request.user.is_authenticated:
            print(request.user.username + " is logged in.")
            login_status = "Welcome back, " + request.user.username + "!"
        else:
            login_status = "Login to post to the message boards."
        return render(
            request,
            'msg_board/index.html',
            {
            'header': self.header,
            'locations': self.l,
            'login_status': login_status,
            'login_form': self.login_form,
            'board_poll_form': self.board_poll_form
            }
            )

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            login_status = "Welcome back, " + user.username +"!"    
        else:
            login_status = "Invalid username and/or password, please try again."
        return render(
                request,
                'msg_board/index.html',
                {
                'login_status': login_status,
                'header': self.header,
                'locations': self.l,
                'board_poll_form': self.board_poll_form
                }
                ) 


class MsgBoardView(LoginRequiredMixin, View):

    def get(self, request, location):
        if request.GET and request.GET['guest'] == 'guest_login':
            username = 'guest'; password = 'password1234'
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
        guest_user = False #initialize this context variable as False so that template renders the msg_form by default
        if request.user.username == 'guest':
            guest_user = True
        msg_form = Msg_boardForm()
        l = Location.objects.get(name=location)
        comment_list = Msg_post.objects.filter(location=l)
        place = l.name.replace('_', ' ')
        return render(
            request,
            'msg_board/msg_board.html',
            {
                'msg_form': msg_form,
                'location': place,
                'comment_list': comment_list,
                'guest_user': guest_user
            }
            )

    def post(self, request, location):
        msg_form = Msg_boardForm()
        if (not request.body) or (len(request.POST['comment'])<4) :
            return HttpResponseRedirect( reverse('msg_board:message_board', args=(location,) ))
        l = Location.objects.get(name=location)
        msg_post = Msg_post(
            username = request.user.username,
            location = l,
            time_of_day = request.POST['time_of_day'],
            quality = request.POST['quality'],
            size = request.POST['size'],
            comment = request.POST['comment']
            )
        msg_post.save()
        comment_list = Msg_post.objects.all()
        return HttpResponseRedirect( reverse('msg_board:message_board', args=(location,) ))


class Board_pollView(View):

    def get_boards(self):
        self.shortboards = Board_choice_poll.objects.filter(board_choice="Shortboard")
        self.number_of_shortboards = len(self.shortboards)
        self.longboards = Board_choice_poll.objects.filter(board_choice="Longboard")
        self.number_of_longboards = len(self.longboards)
        self.fish = Board_choice_poll.objects.filter(board_choice="Fish")
        self.number_of_fish = len(self.fish)
        self.wavestorms = Board_choice_poll.objects.filter(board_choice="Wavestorm")
        self.number_of_wavestorms = len(self.wavestorms)
        self.funboards = Board_choice_poll.objects.filter(board_choice="Funboard")
        self.number_of_funboards = len(self.funboards)
        self.retro = Board_choice_poll.objects.filter(board_choice="Retro")
        self.number_of_retro = len(self.retro)
        self.experimental = Board_choice_poll.objects.filter(board_choice="Experimental")
        self.number_of_experimental = len(self.experimental)

    def post(self, request):
        board_choice_model = Board_choice_poll(
            board_choice = request.POST['board_choice']
        )
        board_choice_model.save()
        return HttpResponseRedirect( reverse('msg_board:message_index') )

    def get(self, request):
        self.get_boards()
        return HttpResponse(
            "Longboards: " + str(self.number_of_longboards) + "\n" +
            "Shortboards: " + str(self.number_of_shortboards) + "\n" +
            "Funboards: " + str(self.number_of_funboards) + "\n" +
            "Wavestorms: " + str(self.number_of_wavestorms) + "\n" +
            "Fish: " + str(self.number_of_fish) + "\n" +
            "Retro: " + str(self.number_of_retro) + "\n" +
            "Experimental: " + str(self.number_of_experimental) + "\n"
            )

