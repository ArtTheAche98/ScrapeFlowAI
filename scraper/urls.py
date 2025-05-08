from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    # Basic stuff
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    # Main
    path('dashboard/', views.dashboard, name='dashboard'),
    path('schedule/add/', views.add_schedule, name='add_schedule'),
    path('schedule/toggle/<int:schedule_id>/', views.toggle_schedule, name='toggle_schedule'),
    path('schedule/delete/<int:schedule_id>/', views.delete_schedule, name='delete_schedule'),
    # LinkedIn
    path('linkedin/settings/', views.linkedin_settings, name='linkedin_settings'),
    path('linkedin/auth/', views.linkedin_auth, name='linkedin_auth'),
    path('linkedin/callback/', views.linkedin_callback, name='linkedin_callback'),
    path('linkedin/remove/', views.remove_linkedin, name='remove_linkedin'),
    # Meta
    path('meta/auth/', views.meta_auth, name='meta_auth'),
    path('meta/callback/', views.meta_callback, name='meta_callback'),
    path('meta/remove/', views.meta_disconnect, name='meta_disconnect'),
    # Telegram
    path('telegram/settings/', views.telegram_settings, name='telegram_settings'),
    path('telegram/disconnect/', views.telegram_disconnect, name='telegram_disconnect'),
    # Password reset
        path('account/settings/', views.account_settings, name='account_settings'),
    path('account/password_change/', auth_views.PasswordChangeView.as_view(
        template_name='scraper/password_change.html',
        success_url='/account/password_change/done/'
    ), name='password_change'),
    path('account/password_change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='scraper/password_change_done.html'
    ), name='password_change_done'),
    path('account/password_reset/', auth_views.PasswordResetView.as_view(
        template_name='scraper/password_reset.html',
        email_template_name='scraper/password_reset_email.html',
        subject_template_name='scraper/password_reset_subject.txt',
        success_url='/account/password_reset/done/'
    ), name='password_reset'),
    path('account/password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='scraper/password_reset_done.html'
    ), name='password_reset_done'),
    path('account/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='scraper/password_reset_confirm.html',
        success_url='/account/reset/done/'
    ), name='password_reset_confirm'),
    path('account/reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='scraper/password_reset_complete.html'
    ), name='password_reset_complete'),
]