from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import views
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

urlpatterns = [


    #path("admin/", admin.site.urls),
    #path('',include('Accounts.urls'))
    path('home/',views.home,name="home"),
   # path('profile/', views.emp_profile, name="emp"),
   # path('hr/',views.hr_home,name="hr_home"),
   # path('manager/',views.manager_home,name="manager_home"),
    path('emplist/',views.Emp_list, name='emp_list'),
    path('total_employees/',views.Total_Employees, name='total_employees'),
    path('total_employees_manager/',views.Total_Employees_manager, name='total_employees_manager'),
    path('role/',views.role, name='role'),
    path('employee_leave/', views.Employee_leave, name='employee_leave'),
    path('company_info/', views.company_info, name='company_info'),
    path('update_company_info/', views.update_company_info_update_data, name='update_company_info'),

    #path('signup/',views.signup_view, name='signup'),
    path('signup/', views.Register_view, name='signup1'),


    path('present_employee/', views.present_employee, name='present_employee'),
    path('absent_employee/', views.absent_employee, name='absent_employee'),
    path('detail/<int:id>/', views.employee_detail, name='detail') ,
    path('company_detail/', views.company_detail, name='company_detail'),
    path('update/<int:id>/', views.update_emp, name='update'),
    path('details/<int:id>/', views.details_view, name='details'),
    #path('hr/details/<int:id>/', views.details_view, name='details') ,
    path('emp/<int:id>/delete', views.delete_emp, name='delete'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('forgot_password/', views.forgot_password,name="forgot_password"),
   # path('password_reset/',auth_views.PasswordResetView.as_view(),name="password_reset"),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name="password_reset_confirm"),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name="password_reset_complete"),
    path('leave-request/',views.leave_request_view, name='leave_request'),
    path('leave-request/success/', views.leave_request_success_view, name='leave_request_success'),
    path('leave-approval/<int:request_id>/', views.leave_approval_view, name='leave_approval'),
    path('leave-approvals_pending/', views.leave_approvals_pending, name='leave_approval_pending'),
    path('leave-requests/', views.leave_request_list_view, name='leave_request_list'),
    path('notifications/', views.notification_view, name='notifications'),
    path('leave_status/',views.leave_verify,name="verify_leave"),



    path('notifyed/<int:id>/',views.Notifyed,name="notifyed"),
    path('permission-request/', views.permission_request_view, name='permission_request'),
    path('permission-request/success/', views.permission_request_success_view, name='permission_request_success'),
    path('permission-approval/<int:request_id>/', views.permission_approval_view, name='permission_approval'),
    path('permission-requests/', views.permission_request_list_view, name='permission_request_list'),
    path('pending_permissions/',views.Pending_permission,name="pending_permission"),
    path('total_pending_permissions/',views.Total_Pending_permission,name="total_pending_permissions"),
    path('attendance/', views.Attendance_view,name='attendance'),
    path('attendence_records/',views.Attndence_Records,name="records"),
    path('punch/',views.punch,name="punch"),
    path('punch_in/',views.punch_in_prasent,name="punch_in"),

    path('test/',views.test,),
    path('calculation/', views.Calculation_view, name="calculate"),
    path('api/events/', views.get_events, name='get_events'),
    #--------
    path("",views.index,name="index"),
    path("faq/", views.faq, name="faq"),
    path("faq_employee/", views.faq_employee, name="faq_employee"),
    path("get/<int:id>/", views.get_item, name="getitem"),
    path("create/",views.create,name="create"),
    path("update_p/<int:id>/", views.update_p, name="up_p"),
    path('my_get_view/',views.my_get_view,name="my_get_view"),
    path("update_emp/<int:id>/", views.index, name="update_emp"),





    #-------------
    path('birthday/',views.birthdays,),
    path('attandrecords/',views.daywise_records,),
    path("birthdate/", views.birthdate, name="birthdate"),

    path("up/<int:id>/",views.emp_update_view,name="up"),
    path("submit_immegration/",views.Add_immegration_data,name="immegration"),
    path("update_immegration/", views.update_immegration_data, name="immegration_update"),
    path("emergency_contacts/",views.Add_emergency_contacts_data,name="contacts"),
    path("social_profile/",views.Add_profile_data,name="profile"),
    path("all_documents/", views.Add_documents_data, name="documents"),
    path("qualifications/", views.Add_qualifications_data, name="qualifications"),
    path("work_experience/", views.Add_work_experience_data, name="experience"),
    path("bank_account/", views.Add_bank_account_data, name="account"),

    path("basic_salary/", views.Add_basic_salary_data, name="basic_salary"),
    path("update_basic_salary/", views.update_basic_salary_data, name="update_basic_salary"),
    path('delete_basic_salary/', views.delete_basic_salary_data, name='delete_basic_salary'),

    path("allowances/", views.Add_allowances_data, name="allowances"),
    path("update_allowances/", views.update_allowances_data, name="update_allowances"),
    path('delete_allowances/', views.delete_allowances_data, name='delete_allowances'),

    path("commissions/", views.Add_commissions_data, name="commissions"),
    path("update_commissions/", views.update_commissions_data, name="update_commissions"),
    path('delete_commissions/', views.delete_commissions_data, name='delete_commissions'),

    path("loan/", views.Add_loan_data, name="loan"),
    path("update_loan/", views.update_loan_data, name="update_loan"),
    path('delete_loan/', views.delete_loan_data, name='delete_loan'),

    path("statutory_deduction/", views.Add_statutory_deduction_data, name="statutory_deduction"),
    path("update_statutory_deduction/", views.update_statutory_deduction_data, name="update_statutory_deduction"),
    path('delete_statutory_deduction/', views.delete_statutory_deduction_data, name='delete_statutory_deduction'),

    path("other_payments/", views.Add_other_payments_data, name="other_payments"),
    path('update_other_payments/', views.update_other_payments_data, name='update_other_payments'),
    path('delete_other_payments/', views.delete_other_payments_data, name='delete_other_payments'),

    path("over_time/", views.Add_over_time_data, name="over_time"),
    path('update_over_time/', views.update_over_time_data, name='update_over_time'),
    path('delete_over_time/', views.delete_over_time_data, name='delete_over_time'),

    path("terminations_get/<int:id>/", views.get_terminations_data, name="terminations_get"),






    path("terminations/", views.Add_terminations_data, name="terminations"),
    path("update_terminations/", views.update_terminations_data, name="update_terminations"),
    path("delete_terminations/", views.delete_terminations_data, name="delete_terminations"),







    path('hr_view/',views.Hr_view ,name="hr_dashboard"),

    path('fetch_festivals/',views.fetch_festivals,name="fetch_festivals"),





    #Holidays
    path("holidays/", views.List_holidays_data, name="list_holidays"),
    path("add_holidays/", views.Adding_holidays_data, name="add_holidays"),
    path("add_holidays_import/", views.Adding_holidays_import_data, name="add_holidays_import"),
    path("update_holidays/<int:id>/", views.update_holidays_data, name="update_holidays"),
    path("delete_holidays/<int:id>/", views.delete_holidays_data, name="delete_holidays"),

    # Tickets
    path("tickets/", views.List_Tickets_data, name="list_tickets"),
    path("add_tickets/", views.Adding_Tickets_data, name="add_tickets"),
    path("update_tickets/<int:id>/", views.update_Tickets_data, name="update_tickets"),
    path("delete_tickets/<int:id>/", views.delete_Tickets_data, name="delete_tickets"),
    path("tickets_reports/", views.Ticket_reports, name="tickets_reports"),
    path("tickets_reports_admin/", views.Ticket_reports_admin, name="tickets_reports_admin"),
    path("tickets_reports_admin_data/", views.Ticket_reports_admin_data, name="tickets_reports_admin_data"),
    path("tickets_approval/<int:id>/", views.Tickets_approval, name="tickets_approval"),

    # Expenses
    path("expenses/", views.List_Expenses_data, name="list_expenses"),
    path("add_expenses/", views.Adding_Expenses_data, name="add_expenses"),
    path("update_expenses/<int:id>/", views.update_Expenses_data, name="update_expenses"),
    path("delete_expenses/<int:id>/", views.delete_Expenses_data, name="delete_expenses"),
    path("expenses_reports/", views.Expenses_reports, name="expenses_reports"),
    path("expenses_reports_admin/", views.Expenses_reports_admin, name="expenses_reports_admin"),
    path("expenses_reports_admin_data/", views.Expenses_reports_admin_data, name="expenses_reports_admin_data"),
    path("expenses_approval/<int:id>/", views.Expenses_approval, name="expenses_approval"),

    #company
    path("company/", views.List_company_data, name="list_company"),
    path("add_company/", views.Add_company_data, name="add_company"),
    path("update_company/<int:id>/", views.update_company_data, name="update_company"),
    path("delete_company/<int:id>/", views.delete_company_data, name="delete_company"),

    # Department
    path("department/", views.List_department_data, name="list_department"),
    path("add_department/", views.Adding_department_data, name="add_department"),
    path("update_department/<int:id>/", views.update_department_data, name="update_department"),
    path("delete_department/<int:id>/", views.delete_department_data, name="delete_department"),
    #location

    path("location/", views.list_location_data, name="list_location"),
    path('add_location/', views.Add_location_data, name='add_location'),
    path("delete_location/<int:id>/", views.delete_location_data, name="delete_location"),
    path("update_location/<int:id>/", views.update_location_data, name="update_location"),

    # Promotions
    path("promotions/", views.List_promotions_data, name="list_promotions"),
    path("add_promotions/", views.Adding_promotions_data, name="add_promotions"),
    path("update_promotions/<int:id>/", views.update_promotions_data, name="update_promotions"),
    path("delete_promotions/<int:id>/", views.delete_promotions_data, name="delete_promotions"),

    # Assets
    path("assets/", views.List_assets_data, name="list_assets"),
    path("add_assets/", views.Adding_assets_data, name="add_assets"),
    path("update_assets/<int:id>/", views.update_assets_data, name="update_assets"),
    path("delete_assets/<int:id>/", views.delete_assets_data, name="delete_assets"),

    # Source
    path("source/", views.List_source_data, name="list_source"),
    path("add_source/", views.Adding_source_data, name="add_source"),
    path("update_source/<int:id>/", views.update_source_data, name="update_source"),
    path("delete_source/<int:id>/", views.delete_source_data, name="delete_source"),

    # Status
    path("status/", views.List_status_data, name="list_status"),
    path("add_status/", views.Adding_status_data, name="add_status"),
    path("update_status/<int:id>/", views.update_status_data, name="update_status"),
    path("delete_status/<int:id>/", views.delete_status_data, name="delete_status"),

    # Priority
    path("priority/", views.List_priority_data, name="list_priority"),
    path("add_priority/", views.Adding_priority_data, name="add_priority"),
    path("update_priority/<int:id>/", views.update_priority_data, name="update_priority"),
    path("delete_priority/<int:id>/", views.delete_priority_data, name="delete_priority"),

    # Category
    path("category/", views.List_category_data, name="list_category"),
    path("add_category/", views.Adding_category_data, name="add_category"),
    path("update_category/<int:id>/", views.update_category_data, name="update_category"),
    path("delete_category/<int:id>/", views.delete_category_data, name="delete_category"),

    # Awards
    path("awards/", views.List_awards_data, name="list_awards"),
    path("add_awards/", views.Adding_awards_data, name="add_awards"),
    path("update_awards/<int:id>/", views.update_awards_data, name="update_awards"),
    path("delete_awards/<int:id>/", views.delete_awards_data, name="delete_awards"),

    # Designation
    path("designation/", views.List_designation_data, name="list_designation"),
    path("add_designation/", views.Adding_designation_data, name="add_designation"),
    path("update_designation/<int:id>/", views.update_designation_data, name="update_designation"),
    path("delete_designation/<int:id>/", views.delete_designation_data, name="delete_designation"),

    # Announcements
    path("announcements/", views.List_announcements_data, name="list_announcements"),
    path("add_announcements/", views.Adding_announcements_data, name="add_announcements"),
    path("update_announcements/<int:id>/", views.update_announcements_data, name="update_announcements"),
    path("delete_announcements/<int:id>/", views.delete_announcements_data, name="delete_announcements"),

    # Company_Policy
    path("policy/", views.List_policy_data, name="list_policy"),
    path("add_policy/", views.Adding_policy_data, name="add_policy"),
    path("update_policy/<int:id>/", views.update_policy_data, name="update_policy"),
    path("delete_policy/<int:id>/", views.delete_policy_data, name="delete_policy"),

    # Clients
    path("clients/", views.List_clients_data, name="list_clients"),
    path("add_clients/", views.Adding_clients_data, name="add_clients"),
    path("update_clients/<int:id>/", views.update_clients_data, name="update_clients"),
    path("delete_clients/<int:id>/", views.delete_clients_data, name="delete_clients"),



    # Travel
    path("travel/", views.List_travel_data, name="list_travel"),
    path("add_travel/", views.Adding_travel_data, name="add_travel"),
    path("update_travel/<int:id>/", views.update_travel_data, name="update_travel"),
    path("delete_travel/<int:id>/", views.delete_travel_data, name="delete_travel"),

    # Transfer
    path("transfer/", views.List_transfer_data, name="list_transfer"),
    path("add_transfer/", views.Adding_transfer_data, name="add_transfer"),
    path("update_transfer/<int:id>/", views.update_transfer_data, name="update_transfer"),
    path("delete_transfer/<int:id>/", views.delete_transfer_data, name="delete_transfer"),

    # Transfer
    path("resignation/", views.List_resignation_data, name="list_resignation"),
    path("add_resignation/", views.Adding_resignation_data, name="add_resignation"),
    path("update_resignation/<int:id>/", views.update_resignation_data, name="update_resignation"),
    path("delete_resignation/<int:id>/", views.delete_resignation_data, name="delete_resignation"),

    # Complains
    path("complains/", views.List_complains_data, name="list_complains"),
    path("add_complains/", views.Adding_complains_data, name="add_complains"),
    path("update_complains/<int:id>/", views.update_complains_data, name="update_complains"),
    path("delete_complains/<int:id>/", views.delete_complains_data, name="delete_complains"),

    # Warnings
    path("warnings/", views.List_warnings_data, name="list_warnings"),
    path("add_warnings/", views.Adding_warnings_data, name="add_warnings"),
    path("update_warnings/<int:id>/", views.update_warnings_data, name="update_warnings"),
    path("delete_warnings/<int:id>/", views.delete_warnings_data, name="delete_warnings"),

    # Job_Post
    path("job_post/", views.List_job_post_data, name="list_job_post"),
    path("add_job_post/", views.Adding_job_post_data, name="add_job_post"),
    path("update_job_post/<int:id>/", views.update_job_post_data, name="update_job_post"),
    path("delete_job_post/<int:id>/", views.delete_job_post_data, name="delete_job_post"),

    # Job_Candidate
    path("job_candidate", views.List_job_candidate_data, name="list_job_candidate"),
    path("add_job_candidate/", views.Adding_job_candidate_data, name="add_job_candidate"),
    path("update_job_candidate/<int:id>/", views.update_job_candidate_data, name="update_job_candidate"),
    path("delete_job_candidate/<int:id>/", views.delete_job_candidate_data, name="delete_job_candidate"),

    # Job_Interview
    path("job_interview", views.List_job_interview_data, name="list_job_interview"),
    path("add_job_interview/", views.Adding_job_interview_data, name="add_job_interview"),
    path("update_job_interview/<int:id>/", views.update_job_interview_data, name="update_job_interview"),
    path("delete_job_interview/<int:id>/", views.delete_job_interview_data, name="delete_job_interview"),

    # Trainer
    path("trainer", views.List_trainer_data, name="list_trainer"),
    path("add_trainer/", views.Adding_trainer_data, name="add_trainer"),
    path("update_trainer/<int:id>/", views.update_trainer_data, name="update_trainer"),
    path("delete_trainer/<int:id>/", views.delete_trainer_data, name="delete_trainer"),

    # Training_Type
    path("training_type", views.List_training_type_data, name="list_training_type"),
    path("add_training_type/", views.Adding_training_type_data, name="add_training_type"),
    path("update_training_type/<int:id>/", views.update_training_type_data, name="update_training_type"),
    path("delete_training_type/<int:id>/", views.delete_training_type_data, name="delete_training_type"),

    # Training_List
    path("training_list", views.List_training_list_data, name="list_training_list"),
    path("add_training_list/", views.Adding_training_list_data, name="add_training_list"),
    path("update_training_list/<int:id>/", views.update_training_list_data, name="update_training_list"),
    path("delete_training_list/<int:id>/", views.delete_training_list_data, name="delete_training_list"),

    # Events
    path("events", views.List_events_data, name="list_events"),
    path("add_events/", views.Adding_events_data, name="add_events"),
    path("update_events/<int:id>/", views.update_events_data, name="update_events"),
    path("delete_events/<int:id>/", views.delete_events_data, name="delete_events"),

    # Meetings
    path("meetings", views.List_meetings_data, name="list_meetings"),
    path("add_meetings/", views.Adding_meetings_data, name="add_meetings"),
    path("update_meetings/<int:id>/", views.update_meetings_data, name="update_meetings"),
    path("delete_meetings/<int:id>/", views.delete_meetings_data, name="delete_meetings"),


    path('role_counts/', views.role_counts, name='role_counts'),

    path('shift_count/', views.shift_count, name='shift_count'),

    path('contacts_data/', views.contacts, name='contacts_data'),
    path('attendence_records/',views.Attndence_Records,name="attendence_records"),

    path("upd/<int:id>/",views.emp_update_view,name="up_emp"),
    path("get_record/<int:data_id>/",views.emp_update_total_view,name="get_record"),
    path("emergency_contacts_update/", views.update_emergency_contacts_data, name="update_contacts"),
    path("emergency_contacts_delete/", views.delete_emergency_contacts_data, name="delete_contacts"),
    path("social_profile/",views.Add_profile_data,name="profile1"),
    path("social_profile_update/", views.update_profile_data, name="profile1_update"),
    path("update_documents/", views.update_documents_data, name="update_documents"),
    path("delete_documents/", views.delete_documents_data, name="delete_documents"),
    path("update_qualifications/", views.update_qualifications_data, name="qualifications_update"),
    path("delete_qualifications/", views.delete_qualifications_data, name="qualifications_delete"),
    path("update_work_experience/", views.update_work_experience_data, name="experience_update"),
    path("delete_work_experience/", views.delete_work_experience_data, name="experience_delete"),
    path("bank_account_update/", views.update_bank_account_data, name="account_update"),
    path("get_bank_account_data/<int:id>/", views.get_bank_account_data, name="account_get"),
    path("bank_account_delete/", views.delete_bank_account_data, name="account_delete"),

    path("delete_allowances/", views.delete_allowances_data, name="delete_allowances"),

    path("basic_salary_get/<int:id>/", views.get_basic_salary_data, name="basic_salary_get"),
    path("allowances_get/<int:id>/", views.get_allowances_data, name="allowances_get"),
    path("commissions_get/<int:id>/", views.get_commissions_data, name="commissions_get"),
    path("loan_get/<int:id>/", views.get_loan_data, name="loan_get"),
    path("statutory_deduction_get/<int:id>/", views.get_statutory_deduction_data, name="statutory_deduction_get"),
    path("other_payments_get/<int:id>/", views.get_other_payments_data, name="other_payments_get"),
    path("over_time_get/<int:id>/", views.get_over_time_data, name="over_time_get"),
    path("qualifications_get/<int:id>/", views.get_qualifications_data, name="qualifications_get"),
    path("documents_get/<int:id>/", views.get_all_documents_data, name="documents_get"),
    path("emergency_contacts_get/<int:id>/", views.get_emergency_contacts_data, name="emergency_contacts_get"),
    path("get_immegration/<int:id>/", views.get_immegration_data, name="get_immegration"),

    path("get_work_experience/<int:id>/", views.get_work_experience_data, name="get_work_experience"),
    path("delete_immegration/", views.delete_immegration_data, name="delete_immegration"),


    path('employee_work/', views.dashboard, name="employee_work"),
    path('hr_my_tasks/', views.hr_dashboard, name="hr_my_tasks"),

    path('completed_tasks_hr/', views.completed_tasks_hr, name="completed_tasks_hr"),
    path('my_tasks_completed/', views.my_tasks_completed, name="my_tasks_completed"),
    path('my_tasks_todo/', views.my_tasks_todo, name="my_tasks_todo"),
    path('my_tasks_inprogress/', views.my_tasks_inprogress, name="my_tasks_inprogress"),
    path('todo_tasks_hr/', views.todo_tasks_hr, name="todo_tasks_hr"),
    path('in_progress_tasks_hr/', views.in_progress_tasks_hr, name="in_progress_tasks_hr"),

    path('completed_tasks/', views.completed_tasks, name="completed_tasks"),
    path('todo_tasks/', views.todo_tasks, name="todo_tasks"),
    path('inprogress_tasks/', views.inprogress_tasks, name="inprogress_tasks"),
    path('hr_attendance_records/',views.Hr_Attendance_Records,name='hr_attendance'),
    path('hr_attendance_monthwise_records/',views.Hr_Attendance_monthwise, name='hr_attendance_records_month'),
    path('hr_attendance_weekwise_records/', views.Hr_Attendance_weekwise, name='hr_attendance_records_week'),
    path('get_departments/<int:company_id>/', views.get_departments, name='get_departments'),
    path('get_employees/<int:department_id>/', views.get_employees, name='get_employees'),



    path("company_info_get/<int:id>/", views.get_company_info_data, name="company_info_get"),

    path('leave_data/', views.leave_data, name='leave_data'),
    path('employee_leaves/', views.employee_leaves, name='employee_leaves'),
    path('employee_details/', views.employee_details, name='employee_details'),

    #project management urls
    path('list_project/', views.List_project_data, name='list_project'),
    path('add_projects/',views.Add_projects, name='add_projects'),
    path('update_projects/<int:id>/', views.Update_project, name='update_project'),
    path('delete_projects/<int:id>/', views.delete_project, name='delete_project'),
    path('emp_list_on_the_project/<int:project_id>/',views.Employee_project,name="emp_on_project"),
   # path("projects_get/<int:id>/", views.get_project_data, name="projects_get"),


 #tasks
    path('get_task_list/', views.tasks, name='task_list'),
    #path('get_task_record/<int:id>/', views.get_taks_record_wise, name='get_project_record'),
    path('add_task/', views.add_my_tasks, name='add_tasks'),
    path('update_task/<int:id>/', views.update_my_tasks_data, name='update_tasks'),


#Email
    path('sent_email/',views.Sent_Email,name="sent_emails"),
    path('receive_emails/', views.Receive_Email, name="receive_emails"),
    path('compose/',views.Compose,name="compose"),
    path('email_details/<int:id>/', views.Email_details, name="details_email"),
    path('sent_email_details/<int:id>/', views.Sent_email_details, name="sent_email_details"),
    path('receive_email_details/<int:id>/', views.Receive_email_details, name="receive_email_details"),


    path('email_delete/', views.Email_delete, name="delete_emails"),
    path('sent_email_delete/<int:id>/', views.delete_sent_Email, name="delete_sent_email"),
    path('receive_email_delete/<int:id>/', views.delete_receive_Email, name="delete_receive_email"),
    path('replay_email/<int:id>/', views.Replay_emails, name="replay_email"),
    path('forward_email/<int:id>/', views.Forword_email, name="forward_email"),


#Email_employee
    path('sent_email_employee/',views.Sent_Email_employee,name="sent_emails_employee"),
    path('receive_emails_employee/', views.Receive_Email_employee, name="receive_emails_employee"),
    path('compose_employee/',views.Compose_employee,name="compose_employee"),
    path('email_details_employee/<int:id>/', views.Email_details_employee, name="details_email_employee"),
    path('sent_email_details_employee/<int:id>/', views.Sent_email_details_employee, name="sent_email_details_employee"),
    path('receive_email_details_employee/<int:id>/', views.Receive_email_details_employee, name="receive_email_details_employee"),


    path('email_delete_employee/', views.Email_delete_employee, name="delete_emails_employee"),
    path('sent_email_delete_employee/<int:id>/', views.delete_sent_Email_employee, name="delete_sent_email_employee"),
    path('receive_email_delete_employee/<int:id>/', views.delete_receive_Email_employee, name="delete_receive_email_employee"),
    path('replay_email_employee/<int:id>/', views.Replay_emails_employee, name="replay_email_employee"),
    path('forward_email_employee/<int:id>/', views.Forword_email_employee, name="forward_email_employee"),

#hr_tasks
    path('tasks_hr_list/', views.List_tasks_hr_data, name="list_tasks_hr"),
    path('tasks_hr_add/', views.Add_tasks_hr, name="add_tasks_hr"),

    # Financial Year
    path("financial_year/", views.List_financial_data, name="list_financial_year"),
    path("add_financial_year/", views.Adding_finanacial_data, name="add_financial_year"),
    path("delete_financial_year/<int:id>/", views.delete_financial_data, name="delete_financial_year"),

    path('create_shift/', views.create_shift, name="create_shift"),
    path('leave_data_employee/', views.leave_data_employee, name="leave_data_employee"),

    path("update_tasks_hr/<int:id>/", views.update_tasks_hr_data, name="update_tasks_hr"),

    path('get_employees_for_project/', views.get_employees_for_project, name='get_employees_for_project'),

    path('import/', views.import_from_excel, name='import_from_excel'),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
