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
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='epistemic_endline_group', to='otree.Session')),
            ],
            options={
                'db_table': 'epistemic_endline_group',
            },
            bases=(models.Model, otree.db.idmap.GroupIDMapMixin),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='epistemic_endline_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'epistemic_endline_subsession',
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
                ('enjoy', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True, verbose_name='')),
                ('partner_valued_me', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True, verbose_name='')),
                ('i_valued_partner', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True, verbose_name='')),
                ('partner_respects_me', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True, verbose_name='')),
                ('i_respect_partner', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True, verbose_name='')),
                ('talking_politics', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True, verbose_name='')),
                ('neighbors', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True, verbose_name='')),
                ('close_friends', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True, verbose_name='')),
                ('son_or_daughter', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True, verbose_name='')),
                ('compromise', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True, verbose_name='')),
                ('valid_arguments', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True, verbose_name='')),
                ('partner_typical_belief', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True, verbose_name='')),
                ('partner_typical_behavior', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True, verbose_name='')),
                ('partner_typical_value', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True, verbose_name='')),
                ('me_respect_for_outparty', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True, verbose_name='')),
                ('partner_respect_for_outparty', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True, verbose_name='')),
                ('suc_courts', otree.db.models.StringField(help_text='When answering, a value of "0" indicates that you are extremely unlikely to vote for the candidate. A value of "100" indicates that you are extremely likely to vote for the candidate', max_length=10000, null=True)),
                ('suc_polling', otree.db.models.StringField(help_text='When answering, a value of "0" indicates that you are extremely unlikely to vote for the candidate. A value of "100" indicates that you are extremely likely to vote for the candidate', max_length=10000, null=True)),
                ('suc_redistricting', otree.db.models.StringField(help_text='When answering, a value of "0" indicates that you are extremely unlikely to vote for the candidate. A value of "100" indicates that you are extremely likely to vote for the candidate', max_length=10000, null=True)),
                ('suc_election_results', otree.db.models.StringField(help_text='When answering, a value of "0" indicates that you are extremely unlikely to vote for the candidate. A value of "100" indicates that you are extremely likely to vote for the candidate', max_length=10000, null=True)),
                ('performance_estimate', otree.db.models.FloatField(null=True, verbose_name='What percent of teams do you believe performed worse than your team? An answer of 100 implies that you believe 100% of other teams in this study performed worse than your team. An answer of 0 implies that you believe 0% of teams performed worse than your team.')),
                ('perfect_partner_politics', otree.db.models.StringField(help_text='When answering, a value of "0" indicates that your ideal partner, if invited to play this game again in the future, would be strongly liberal. A value of "100" indicates that your ideal partner would be strongly conservative.', max_length=10000, null=True, verbose_name='Perfect Partner Politics: If given the opportunity to play this game again with a partner of your choosing, how strongly liberal or conservative would you prefer they be?')),
                ('partner_benefit', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True, verbose_name='')),
                ('better_performance', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True, verbose_name='')),
                ('feelings_thermometer_repub', otree.db.models.FloatField(help_text="We'd again like to get your feelings toward REPUBLICANS in the U.S. on a 'feeling thermometer.' A rating of zero degrees means you feel as cold and negative as possible. A rating of 100 degrees means you feel as warm and positive as possible. You would rate the group at 50 degrees if you don’t feel particularly positive or negative toward the group.", null=True, verbose_name='How do you feel about REPUBLICANS?')),
                ('feelings_thermometer_democrat', otree.db.models.FloatField(help_text="We'd again like to get your feelings toward DEMOCRATS in the U.S. on a 'feeling thermometer.' A rating of zero degrees means you feel as cold and negative as possible. A rating of 100 degrees means you feel as warm and positive as possible. You would rate the group at 50 degrees if you don’t feel particularly positive or negative toward the group.  How do you feel about DEMOCRATS?", null=True, verbose_name='How do you feel about DEMOCRATS?')),
                ('meta_feelings_thermometer_repub', otree.db.models.FloatField(help_text="Using the same feeling thermometer measure as above, how do you think the average REPUBLICAN feels toward DEMOCRATS in the United States? A rating of zero degrees means you believe the average REPUBLICAN feels as cold and negative as possible toward DEMOCRATS. A rating of 100 degrees means you feel believe that the average REPUBLICANS feels as warm and positive as possible toward DEMOCRATS. You would select a rating of 50 degrees if you believe that REPUBLICANS don't feel particularly positive or negative toward DEMOCRATS.", null=True, verbose_name='How do you think the average REPUBLICAN feels about DEMOCRATS?')),
                ('meta_feelings_thermometer_democrat', otree.db.models.FloatField(help_text="Using the same feeling thermometer measure as above, how do you think the average DEMOCRAT feels toward REPUBLICANS? in the United States? A rating of zero degrees means you believe the average DEMOCRAT feels as cold and negative as possible toward REPUBLICANS. A rating of 100 degrees means you feel believe that the average DEMOCRAT feels as warm and positive as possible toward REPUBLICANS. You would select a rating of 50 degrees if you believe that DEMOCRATS don't feel particularly positive or negative toward REPUBLICANS.", null=True, verbose_name='How do you think the average DEMOCRAT feels about REPUBLICANS?')),
                ('fairness', otree.db.models.FloatField(null=True, verbose_name='How biased against your political affiliation did you feel the questions in this game were?')),
                ('researcher_trust', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True, verbose_name='')),
                ('demand_effects', otree.db.models.LongStringField(null=True, verbose_name="What do you think the goal of this study was? If you don't know, you can just say 'don't know'")),
                ('feedback_partner', otree.db.models.LongStringField(null=True, verbose_name='Please share with us any thoughts you have about your partner. Did you enjoy working with them? Did you feel that you benefitted from having them on your team?')),
                ('feedback_game', otree.db.models.LongStringField(null=True, verbose_name='What did you think about the game? Do you have any feedback to share with us?')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='epistemic_endline.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='epistemic_endline_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='epistemic_endline_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epistemic_endline.Subsession')),
            ],
            options={
                'db_table': 'epistemic_endline_player',
            },
            bases=(models.Model, otree.db.idmap.PlayerIDMapMixin),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epistemic_endline.Subsession'),
        ),
    ]