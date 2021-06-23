# Generated by Django 2.2.12 on 2021-06-16 16:54

from django.db import migrations, models
import django.db.models.deletion
import otree.db.idmap
import otree.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_group', to='otree.Session')),
            ],
            options={
                'db_table': 'quiz_group',
            },
            bases=(models.Model, otree.db.idmap.GroupIDMapMixin),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quiz_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'quiz_subsession',
            },
            bases=(models.Model, otree.db.idmap.SubsessionIDMapMixin),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_role', otree.db.models.StringField(max_length=10000, null=True)),
                ('trial_counter', otree.db.models.IntegerField(default=0, null=True)),
                ('question_id', otree.db.models.IntegerField(null=True)),
                ('question', otree.db.models.StringField(max_length=10000, null=True)),
                ('solution', otree.db.models.StringField(max_length=10000, null=True)),
                ('submitted_answer', otree.db.models.StringField(max_length=10000, null=True)),
                ('confidence', otree.db.models.FloatField(null=True)),
                ('submitted_answer_private', otree.db.models.StringField(max_length=10000, null=True)),
                ('confidence_private', otree.db.models.FloatField(null=True)),
                ('total_score', otree.db.models.IntegerField(default=0, null=True)),
                ('group_score', otree.db.models.IntegerField(default=0, null=True)),
                ('round_payout', otree.db.models.FloatField(default=0, null=True)),
                ('total_payout', otree.db.models.FloatField(default=0, null=True)),
                ('blur_quantity', otree.db.models.IntegerField(default=0, null=True)),
                ('chat_question', otree.db.models.StringField(max_length=10000, null=True)),
                ('chat_results', otree.db.models.StringField(max_length=10000, null=True)),
                ('rescue_event', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True)),
                ('drag_down', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True)),
                ('cheat_consent', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, null=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Subsession')),
            ],
            options={
                'db_table': 'quiz_player',
            },
            bases=(models.Model, otree.db.idmap.PlayerIDMapMixin),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Subsession'),
        ),
    ]