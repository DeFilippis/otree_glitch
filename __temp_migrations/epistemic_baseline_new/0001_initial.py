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
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='epistemic_baseline_new_group', to='otree.Session')),
            ],
            options={
                'db_table': 'epistemic_baseline_new_group',
            },
            bases=(models.Model, otree.db.idmap.GroupIDMapMixin),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='epistemic_baseline_new_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'epistemic_baseline_new_subsession',
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
                ('turk_id', otree.db.models.StringField(help_text='Please make sure this is correct, since we use this to validate your payment.', max_length=10000, null=True, verbose_name='What is your TurkID?')),
                ('sex', otree.db.models.StringField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10000, null=True, verbose_name='What is your biological sex?')),
                ('birth', otree.db.models.IntegerField(null=True, verbose_name='What year were you born?')),
                ('race', otree.db.models.StringField(choices=[('White', 'White'), ('Black or African American', 'Black or African American'), ('Asian', 'Asian'), ('American Indian or Alaska Native', 'American Indian or Alaska Native'), ('Native Hawaiian or Pacific Islander', 'Native Hawaiian or Pacific Islander'), ('Other', 'Other')], max_length=10000, null=True, verbose_name='What race do you most identify with?')),
                ('hispanic', otree.db.models.StringField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10000, null=True, verbose_name='Do you consider yourself Spanish, Hispanic, or Latino?')),
                ('education', otree.db.models.StringField(choices=[('Less than High School', 'Less than High School'), ('H.S. Graduate', 'H.S. Graduate'), ('Some College', 'Some College'), ("Associate's Degree", "Associate's Degree"), ('College Graduate', 'College Graduate'), ("Master's Degree", "Master's Degree"), ('Professional Degree (JD/MD), PhD', 'Professional Degree (JD/MD), PhD')], max_length=10000, null=True, verbose_name='What is the highest level of education that you have achieved?')),
                ('income', otree.db.models.StringField(choices=[('Less than $10,000', 'Less than $10,000'), ('$10,000 to $19,999', '$10,000 to $19,999'), ('$20,000 to $29,999', '$20,000 to $29,999'), ('$30,000 to $39,999', '$30,000 to $39,999'), ('$40,000 to $49,999', '$40,000 to $49,999'), ('$50,000 to $59,999', '$50,000 to $59,999'), ('$60,000 to $69,999', '$60,000 to $69,999'), ('$70,000 to $79,999', '$70,000 to $79,999'), ('$80,000 to $89,999', '$80,000 to $89,999'), ('$90,000 to $99,999', '$90,000 to $99,999'), ('$100,000 to $149,999', '$100,000 to $149,999'), ('$150,000 or more', '$150,000 or more')], max_length=10000, null=True, verbose_name='Which of the following best represents your household income last year before taxes?')),
                ('zip_code', otree.db.models.StringField(max_length=10000, null=True, verbose_name='What is your current zip code?')),
                ('turk_experience', otree.db.models.IntegerField(help_text="Enter a number between 0 and 1,000,000. Try your best to estimate about how many studies you've completed becoming an MTurker.", null=True, verbose_name='About how many total academic studies have you done on MTurk?')),
                ('trust_daily', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True, verbose_name='')),
                ('politics_today', otree.db.models.StringField(choices=[('Strong Democrat', 'Strong Democrat'), ('Weak Democrat', 'Weak Democrat'), ('Strong Republican', 'Strong Republican'), ('Weak Republican', 'Weak Republican'), ('Independent', 'Independent')], max_length=10000, null=True, verbose_name='In politics TODAY, do you consider yourself a Republican, Democrat, or Independent?')),
                ('politics', otree.db.models.StringField(choices=[('Republican', 'Republican'), ('Democrat', 'Democrat')], max_length=10000, null=True, verbose_name='As of today, do you lean more to the Republican Party or more to the Democratic Party?')),
                ('political_views', otree.db.models.StringField(choices=[('Very Liberal', 'Very Liberal'), ('Mostly Liberal', 'Mostly Liberal'), ('Somewhat Liberal', 'Somewhat Liberal'), ('Moderate', 'Moderate'), ('Somewhat Conservative', 'Somewhat Conservative'), ('Mostly Conservative', 'Mostly Conservative'), ('Very Conservative', 'Very Conservative')], max_length=10000, null=True, verbose_name='Which of the following best describes your political views?')),
                ('political_views_granular', otree.db.models.FloatField(null=True, verbose_name='Which point on this scale best describes your political views?')),
                ('feelings_thermometer_repub', otree.db.models.FloatField(help_text="We'd like to get your feelings toward REPUBLICANS in the U.S. on a 'feeling thermometer.' A rating of zero degrees means you feel as cold and negative as possible. A rating of 100 degrees means you feel as warm and positive as possible. You would rate the group at 50 degrees if you don’t feel particularly positive or negative toward the group.", null=True, verbose_name='How do you feel about REPUBLICANS?')),
                ('feelings_thermometer_democrat', otree.db.models.FloatField(help_text="We'd like to get your feelings toward DEMOCRATS in the U.S. on a 'feeling thermometer.' A rating of zero degrees means you feel as cold and negative as possible. A rating of 100 degrees means you feel as warm and positive as possible. You would rate the group at 50 degrees if you don’t feel particularly positive or negative toward the group.  How do you feel about DEMOCRATS?", null=True, verbose_name='How do you feel about DEMOCRATS?')),
                ('meta_feelings_thermometer_repub', otree.db.models.FloatField(help_text="Using the same feeling thermometer measure as above, how do you think the average REPUBLICAN feels toward DEMOCRATS in the United States? A rating of zero degrees means you believe the average REPUBLICAN feels as cold and negative as possible toward DEMOCRATS. A rating of 100 degrees means you feel believe that the average REPUBLICANS feels as warm and positive as possible toward DEMOCRATS. You would select a rating of 50 degrees if you believe that REPUBLICANS don't feel particularly positive or negative toward DEMOCRATS.", null=True, verbose_name='How do you think the average REPUBLICAN feels about DEMOCRATS?')),
                ('meta_feelings_thermometer_democrat', otree.db.models.FloatField(help_text="Using the same feeling thermometer measure as above, how do you think the average DEMOCRAT feels toward REPUBLICANS? in the United States? A rating of zero degrees means you believe the average DEMOCRAT feels as cold and negative as possible toward REPUBLICANS. A rating of 100 degrees means you feel believe that the average DEMOCRAT feels as warm and positive as possible toward REPUBLICANS. You would select a rating of 50 degrees if you believe that DEMOCRATS don't feel particularly positive or negative toward REPUBLICANS.", null=True, verbose_name='How do you think the average DEMOCRAT feels about REPUBLICANS?')),
                ('superpower', otree.db.models.StringField(choices=[('Invisibility', 'Invisibility'), ('Super Strength', 'Super Strength'), ('Ultra High Intelligence', 'Ultra High Intelligence'), ('Flight', 'Flight')], max_length=10000, null=True, verbose_name='Which of the following superpowers would you most prefer to have?')),
                ('season', otree.db.models.StringField(choices=[('Winter', 'Winter'), ('Summer', 'Summer'), ('Fall', 'Fall'), ('Spring', 'Spring')], max_length=10000, null=True, verbose_name='Which of the following seasons are your favorite?')),
                ('fruit', otree.db.models.StringField(choices=[('Pineapple', 'Pineapple'), ('Mango', 'Mango'), ('Blueberry', 'Blueberry'), ('Banana', 'Banana')], max_length=10000, null=True, verbose_name='Which of the following fruits do you most enjoy eating?')),
                ('vacation', otree.db.models.StringField(choices=[('Mountains', 'Mountains'), ('Forest', 'Forest'), ('Beach', 'Beach'), ('City', 'City')], max_length=10000, null=True, verbose_name='Where would you most enjoy vacationing?')),
                ('political_inconsistency', otree.db.models.IntegerField(default=0, null=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='epistemic_baseline_new.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='epistemic_baseline_new_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='epistemic_baseline_new_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epistemic_baseline_new.Subsession')),
            ],
            options={
                'db_table': 'epistemic_baseline_new_player',
            },
            bases=(models.Model, otree.db.idmap.PlayerIDMapMixin),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epistemic_baseline_new.Subsession'),
        ),
    ]
