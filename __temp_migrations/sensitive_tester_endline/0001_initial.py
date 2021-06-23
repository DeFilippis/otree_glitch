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
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sensitive_tester_endline_group', to='otree.Session')),
            ],
            options={
                'db_table': 'sensitive_tester_endline_group',
            },
            bases=(models.Model, otree.db.idmap.GroupIDMapMixin),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sensitive_tester_endline_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'sensitive_tester_endline_subsession',
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
                ('sex', otree.db.models.StringField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10000, null=True, verbose_name='What is your biological sex?')),
                ('birth', otree.db.models.IntegerField(null=True, verbose_name='What year were you born?')),
                ('race', otree.db.models.StringField(choices=[('White', 'White'), ('Black or African American', 'Black or African American'), ('Asian', 'Asian'), ('American Indian or Alaska Native', 'American Indian or Alaska Native'), ('Native Hawaiian or Pacific Islander', 'Native Hawaiian or Pacific Islander')], max_length=10000, null=True, verbose_name='What race do you most identify with?')),
                ('education', otree.db.models.StringField(choices=[('Less than High School', 'Less than High School'), ('H.S. Graduate', 'H.S. Graduate'), ('Some College', 'Some College'), ("Associate's Degree", "Associate's Degree"), ('College Graduate', 'College Graduate'), ("Master's Degree", "Master's Degree"), ('Professional Degree (JD/MD), PhD', 'Professional Degree (JD/MD), PhD')], max_length=10000, null=True, verbose_name='What is the highest level of education that you have achieved?')),
                ('income', otree.db.models.StringField(choices=[('Less than $10,000', 'Less than $10,000'), ('$10,000 to $19,999', '$10,000 to $19,999'), ('$20,000 to $29,999', '$20,000 to $29,999'), ('$30,000 to $39,999', '$30,000 to $39,999'), ('$40,000 to $49,999', '$40,000 to $49,999'), ('$50,000 to $59,999', '$50,000 to $59,999'), ('$60,000 to $69,999', '$60,000 to $69,999'), ('$70,000 to $79,999', '$70,000 to $79,999'), ('$80,000 to $89,999', '$80,000 to $89,999'), ('$90,000 to $99,999', '$90,000 to $99,999'), ('$100,000 to $149,999', '$100,000 to $149,999'), ('$150,000 or more', '$150,000 or more')], max_length=10000, null=True, verbose_name='Which of the following best represents your household income last year before taxes?')),
                ('feedback', otree.db.models.LongStringField(null=True, verbose_name='Do you have any feedback for us?  Did you enjoy the experiment?  Any complaints?')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sensitive_tester_endline.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sensitive_tester_endline_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sensitive_tester_endline_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensitive_tester_endline.Subsession')),
            ],
            options={
                'db_table': 'sensitive_tester_endline_player',
            },
            bases=(models.Model, otree.db.idmap.PlayerIDMapMixin),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensitive_tester_endline.Subsession'),
        ),
    ]