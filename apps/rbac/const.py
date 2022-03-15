from django.db import models
from django.utils.translation import ugettext_lazy as _


class Scope(models.TextChoices):
    system = 'system', _('System')
    org = 'org', _('Organization')


exclude_permissions = (
    # ('App', 'Model', 'Action', 'Resource') Model 和 Resource 可能不同
    # users.add_user
    ('auth', '*', '*', '*'),
    ('captcha', '*', '*', '*'),
    ('contenttypes', '*', '*', '*'),
    ('django_cas_ng', '*', '*', '*'),
    ('django_celery_beat', '*', '*', '*'),
    ('jms_oidc_rp', '*', '*', '*'),
    ('admin', '*', '*', '*'),
    ('sessions', '*', '*', '*'),
    ('notifications', '*', '*', '*'),
    ('common', 'setting', '*', '*'),

    ('authentication', 'privatetoken', '*', '*'),
    ('authentication', 'accesskey', 'change,delete', 'accesskey'),
    ('authentication', 'connectiontoken', 'change,delete', 'connectiontoken'),
    ('authentication', 'ssotoken', 'change,delete', 'ssotoken'),
    ('authentication', 'superconnectiontoken', 'change,delete', 'superconnectiontoken'),
    ('users', 'userpasswordhistory', '*', '*'),
    ('applications', 'applicationuser', '*', '*'),
    ('applications', 'historicalaccount', '*', '*'),
    ('applications', 'account', 'add,change', 'account'),
    ('assets', 'adminuser', '*', '*'),
    ('assets', 'assetgroup', '*', '*'),
    ('assets', 'cluster', '*', '*'),
    ('assets', 'favoriteasset', '*', '*'),
    ('assets', 'historicalauthbook', '*', '*'),
    ('assets', 'assetuser', '*', '*'),
    ('assets', 'gathereduser', 'add,delete,change', 'gathereduser'),
    ('assets', 'accountbackupplanexecution', 'delete,change', 'accountbackupplanexecution'),
    ('assets', 'authbook', 'add,change', 'authbook'),
    ('perms', 'userassetgrantedtreenoderelation', '*', '*'),
    ('perms', 'usergrantedmappingnode', '*', '*'),
    ('perms', 'permnode', '*', '*'),
    ('perms', 'rebuildusertreetask', '*', '*'),
    ('perms', 'permedasset', 'add,change,delete', 'permedasset'),
    ('perms', 'permedapplication', 'add,change,delete', 'permedapplication'),
    ('rbac', 'contenttype', '*', '*'),
    ('rbac', 'permission', 'add,delete,change', 'permission'),
    ('rbac', 'rolebinding', '*', '*'),
    ('rbac', 'role', '*', '*'),
    ('ops', 'adhoc', 'delete,change', '*'),
    ('ops', 'adhocexecution', 'delete,change', '*'),
    ('ops', 'celerytask', '*', '*'),
    ('ops', 'task', 'add,change', 'task'),
    ('ops', 'commandexecution', 'delete,change', 'commandexecution'),
    ('orgs', 'organizationmember', '*', '*'),
    ('settings', 'setting', 'add,change,delete', 'setting'),
    ('audits', 'operatelog', 'add,delete,change', 'operatelog'),
    ('audits', 'passwordchangelog', 'add,change,delete', 'passwordchangelog'),
    ('audits', 'userloginlog', 'add,change,delete,change', 'userloginlog'),
    ('audits', 'ftplog', 'change,delete', 'ftplog'),
    ('tickets', 'ticketassignee', '*', 'ticketassignee'),
    ('tickets', 'ticketflow', 'add,delete', 'ticketflow'),
    ('tickets', 'comment', 'change,delete', 'comment'),
    ('tickets', 'ticket', 'delete', 'ticket'),
    ('tickets', 'ticketstep', '*', '*'),
    ('tickets', 'approvalrule', '*', '*'),
    ('tickets', 'superticket', 'delete', 'superticket'),
    ('tickets', 'ticketsession', 'delete', 'ticketsession'),
    ('xpack', 'interface', '*', '*'),
    ('xpack', 'license', '*', '*'),
    ('xpack', 'syncinstancedetail', 'add,delete,change', 'syncinstancedetail'),
    ('xpack', 'syncinstancetaskexecution', 'delete,change', 'syncinstancetaskexecution'),
    ('xpack', 'changeauthplanexecution', 'delete,change', 'changeauthplanexecution'),
    ('xpack', 'changeauthplantask', 'add,delete', 'changeauthplantask'),
    ('common', 'permission', 'add,delete,view,change', 'permission'),
    ('terminal', 'command', 'delete,change', 'command'),
    ('terminal', 'status', 'delete,change', 'status'),
    ('terminal', 'sessionjoinrecord', 'delete', 'sessionjoinrecord'),
    ('terminal', 'sessionreplay', 'add,change,delete', 'sessionreplay'),
    ('terminal', 'sessionsharing', 'view,add,change,delete', 'sessionsharing'),
    ('terminal', 'session', 'delete,share', 'session'),
    ('terminal', 'session', 'delete,change', 'command'),
)


only_system_permissions = (
    ('assets', 'platform', '*', '*'),
    ('users', 'user', 'delete', 'user'),
    ('rbac', 'role', 'delete,add,change', 'role'),
    ('rbac', 'systemrole', '*', '*'),
    ('rbac', 'rolebinding', '*', '*'),
    ('rbac', 'systemrolebinding', '*', '*'),
    ('rbac', 'orgrole', 'delete,add,change', '*'),
    ('orgs', 'organization', '*', '*'),
    ('xpack', 'license', '*', '*'),
    ('settings', 'setting', '*', '*'),
    ('ops', 'task', 'view', 'taskmonitor'),
    ('terminal', 'terminal', '*', '*'),
    ('terminal', 'commandstorage', '*', '*'),
    ('terminal', 'replaystorage', '*', '*'),
    ('terminal', 'status', '*', '*'),
    ('terminal', 'task', '*', '*'),
    ('tickets', 'ticketflow', '*', '*'),
)

only_org_permissions = (
)

system_exclude_permissions = list(exclude_permissions) + list(only_org_permissions)
org_exclude_permissions = list(exclude_permissions) + list(only_system_permissions)
