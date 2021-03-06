# Generated by Django 2.2.12 on 2021-06-22 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trivia_glitch', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='blur_count_joint',
        ),
        migrations.RemoveField(
            model_name='player',
            name='blur_count_private',
        ),
        migrations.RemoveField(
            model_name='player',
            name='chat_content_joint',
        ),
        migrations.RemoveField(
            model_name='player',
            name='chat_content_results',
        ),
        migrations.RemoveField(
            model_name='player',
            name='cheat_consent',
        ),
        migrations.RemoveField(
            model_name='player',
            name='confidence_joint',
        ),
        migrations.RemoveField(
            model_name='player',
            name='confidence_private',
        ),
        migrations.RemoveField(
            model_name='player',
            name='corrected_private',
        ),
        migrations.RemoveField(
            model_name='player',
            name='drag_down',
        ),
        migrations.RemoveField(
            model_name='player',
            name='idle_joint',
        ),
        migrations.RemoveField(
            model_name='player',
            name='idle_private',
        ),
        migrations.RemoveField(
            model_name='player',
            name='is_inactive',
        ),
        migrations.RemoveField(
            model_name='player',
            name='my_chat_joint',
        ),
        migrations.RemoveField(
            model_name='player',
            name='my_chat_results',
        ),
        migrations.RemoveField(
            model_name='player',
            name='question_choice_1',
        ),
        migrations.RemoveField(
            model_name='player',
            name='question_choice_2',
        ),
        migrations.RemoveField(
            model_name='player',
            name='question_choice_3',
        ),
        migrations.RemoveField(
            model_name='player',
            name='question_choice_4',
        ),
        migrations.RemoveField(
            model_name='player',
            name='question_id',
        ),
        migrations.RemoveField(
            model_name='player',
            name='question_solution',
        ),
        migrations.RemoveField(
            model_name='player',
            name='question_text',
        ),
        migrations.RemoveField(
            model_name='player',
            name='question_type',
        ),
        migrations.RemoveField(
            model_name='player',
            name='rescue_event',
        ),
        migrations.RemoveField(
            model_name='player',
            name='round_payout',
        ),
        migrations.RemoveField(
            model_name='player',
            name='round_total',
        ),
        migrations.RemoveField(
            model_name='player',
            name='submitted_answer_joint',
        ),
        migrations.RemoveField(
            model_name='player',
            name='submitted_answer_private',
        ),
        migrations.RemoveField(
            model_name='player',
            name='time_spent_on_page_joint',
        ),
        migrations.RemoveField(
            model_name='player',
            name='time_spent_on_page_private',
        ),
        migrations.RemoveField(
            model_name='player',
            name='total_score',
        ),
        migrations.RemoveField(
            model_name='player',
            name='trial_counter',
        ),
        migrations.RemoveField(
            model_name='player',
            name='uncorrected_private',
        ),
    ]
