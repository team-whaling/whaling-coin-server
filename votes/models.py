from django.db import models

class AccountUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user_id = models.BigIntegerField(primary_key=True)
    nickname = models.CharField(unique=True, max_length=20)
    acc_percent = models.FloatField()
    point = models.IntegerField()
    profile_img = models.CharField(max_length=200, blank=True, null=True)
    is_default_profile = models.IntegerField()
    is_active = models.IntegerField()
    is_staff = models.IntegerField()
    is_superuser = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'account_user'


class AccountUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AccountUser, on_delete=models.CASCADE)
    group = models.ForeignKey('AuthGroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_user_groups'
        unique_together = (('user', 'group'),)


class AccountUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AccountUser, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AccountUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

class VoteCoin(models.Model):
    coin_code = models.CharField(primary_key=True, max_length=10)
    coin_krname = models.CharField(max_length=12)
    coin_name = models.CharField(max_length=30)
    coin_image = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'vote_coin'

class VoteVote(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    vote_id = models.BigAutoField(primary_key=True)
    state = models.IntegerField()
    finished_at = models.DateTimeField()
    tracked_at = models.DateTimeField()
    created_price = models.IntegerField()
    finished_price = models.IntegerField(blank=True, null=True)
    spent_point = models.IntegerField()
    earned_point = models.IntegerField()
    is_answer = models.IntegerField(blank=True, null=True)
    duration = models.CharField(max_length=10)
    range = models.IntegerField()
    comment = models.CharField(max_length=10)
    pos_participants = models.IntegerField()
    neg_participants = models.IntegerField()
    pos_whales = models.IntegerField()
    neg_whales = models.IntegerField()
    coin = models.ForeignKey(
        VoteCoin,
        on_delete=models.CASCADE,
        verbose_name='투표를 생성할 코인의 종류',
    )
    uploader = models.ForeignKey(AccountUser,
                                 on_delete=models.CASCADE,
                                 verbose_name='투표를 생성한 유저',
                                 related_name='created_votes',
                                 related_query_name='created_vote'
                                 )
    total_participants = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vote_vote'
        app_label = 'vote_db1'

class VoteChoice(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    choice_id = models.BigAutoField(primary_key=True)
    choice = models.IntegerField()
    is_answer = models.IntegerField(blank=True, null=True)
    participant = models.ForeignKey(AccountUser, on_delete=models.CASCADE)
    vote = models.ForeignKey(VoteVote, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'vote_choice'
        app_label = 'vote_db1'


