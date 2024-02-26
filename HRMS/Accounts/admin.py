

from django.contrib import admin
from .models import EmployeeMaster,Pro,Gender,MaratialStatus,StateMaster,ShiftMaster,InterviewMaster,InterviewMasterAssigned,InterviewAttachment,HolidayMaster,EmployeeTypeMaster,EmployeeRoleMaster,InterviewMaster,InterviewMasterAssigned,EmployeeWorkingDay
# Register your models here.,
from .models import Event,Permission
from.models import LeaveRequest,Leavecategory,LeaveApproval,LeaveBalance,Company_Info,CustomUser,Department,Company
admin.site.register(CustomUser)
admin.site.register(Company)
admin.site.register(Department)
admin.site.register(Company_Info)
admin.site.register(Pro)
admin.site.register(MaratialStatus)
admin.site.register(StateMaster)
admin.site.register(ShiftMaster)
admin.site.register(EmployeeMaster)
admin.site.register(Permission)
admin.site.register(LeaveRequest)
admin.site.register(LeaveBalance)
admin.site.register(Leavecategory)
admin.site.register(LeaveApproval)
admin.site.register(Event)
#admin.site.register(LeaveCategoryMaster)
#admin.site.register(EmployeeLeaveMaster)
admin.site.register(InterviewMaster)
admin.site.register(InterviewMasterAssigned)
admin.site.register(InterviewAttachment)

admin.site.register(HolidayMaster)
admin.site.register(EmployeeTypeMaster)
#admin.site.register(EmployeeLeaveCategory)
#admin.site.register()
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    search_fields = ('username',)
    fieldsets = (
        (None, {
            'classes': ['wide'],
            'fields': ('username', 'password')
        }),
        ('Informations personnelles', {
            'classes': ['wide'],
            'fields': ('first_name', 'last_name', 'email', 'avatar')
        }),
        ('Permissions', {
            'classes': ['wide'],
            'fields': ('is_superuser', 'is_staff', 'is_active', 'groups', 'permissions')
        }),
        ('Dates importantes', {
            'classes': ['wide'],
            'fields': ('last_login', 'date_joined')
        }),
    )
    filter_horizontal = ('groups', 'user_permissions',)
