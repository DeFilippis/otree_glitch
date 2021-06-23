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
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outgroup_giving_game_group', to='otree.Session')),
            ],
            options={
                'db_table': 'outgroup_giving_game_group',
            },
            bases=(models.Model, otree.db.idmap.GroupIDMapMixin),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='outgroup_giving_game_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'outgroup_giving_game_subsession',
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
                ('explain_decision_ogg', otree.db.models.LongStringField(null=True, verbose_name='Please explain, in as much detail as possible, why you made the decision you did')),
                ('guess_republican_sent_ogg', otree.db.models.CurrencyField(null=True, verbose_name='How much money do you believe the average Republican sent to a Democrat in this game?')),
                ('guess_democrat_sent_ogg', otree.db.models.CurrencyField(null=True, verbose_name='How much money do you believe the average Democrat sent to a Republican in this game?')),
                ('sent_amount_outgroup', otree.db.models.CurrencyField(default=0, null=True, verbose_name='')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='outgroup_giving_game.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outgroup_giving_game_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outgroup_giving_game_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='outgroup_giving_game.Subsession')),
            ],
            options={
                'db_table': 'outgroup_giving_game_player',
            },
            bases=(models.Model, otree.db.idmap.PlayerIDMapMixin),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='outgroup_giving_game.Subsession'),
        ),
    ]
