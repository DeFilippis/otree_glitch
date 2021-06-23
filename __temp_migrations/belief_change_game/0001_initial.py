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
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='belief_change_game_group', to='otree.Session')),
            ],
            options={
                'db_table': 'belief_change_game_group',
            },
            bases=(models.Model, otree.db.idmap.GroupIDMapMixin),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='belief_change_game_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'belief_change_game_subsession',
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
                ('questions_for_player', otree.db.models.StringField(max_length=10000, null=True)),
                ('question_id', otree.db.models.StringField(max_length=10000, null=True)),
                ('question_text', otree.db.models.StringField(max_length=10000, null=True)),
                ('question_solution', otree.db.models.StringField(max_length=10000, null=True)),
                ('question_type', otree.db.models.StringField(max_length=10000, null=True)),
                ('submitted_answer', otree.db.models.StringField(max_length=10000, null=True)),
                ('blur_count', otree.db.models.IntegerField(default=0, null=True)),
                ('time_spent_on_page', otree.db.models.FloatField(null=True)),
                ('confidence', otree.db.models.FloatField(null=True, verbose_name='How confident do you feel in this answer?')),
                ('partisan_advantage', otree.db.models.StringField(choices=[('Democrat', 'Democrat'), ('Republican', 'Republican')], max_length=10000, null=True, verbose_name='Do you think a Democrat or a Republican would be more likely to know the answer to this question?')),
                ('partisan_advantage_confidence', otree.db.models.FloatField(help_text='Please answer as accurately as possible, as the most accurate participants will be bonused $5.00', null=True, verbose_name='How confident are you in that choice?')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='belief_change_game.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='belief_change_game_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='belief_change_game_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='belief_change_game.Subsession')),
            ],
            options={
                'db_table': 'belief_change_game_player',
            },
            bases=(models.Model, otree.db.idmap.PlayerIDMapMixin),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='belief_change_game.Subsession'),
        ),
    ]
