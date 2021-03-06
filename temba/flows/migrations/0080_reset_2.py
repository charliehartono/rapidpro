# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-06 22:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flows', '0079_reset_1'),
        ('orgs', '0029_reset_1'),
        ('msgs', '0075_reset_1'),
        ('contacts', '0046_reset_1'),
        ('channels', '0053_reset_4'),
    ]

    operations = [
        migrations.AddField(
            model_name='flowstep',
            name='broadcasts',
            field=models.ManyToManyField(help_text='Any broadcasts that are associated with this step (only sent)', related_name='steps', to='msgs.Broadcast'),
        ),
        migrations.AddField(
            model_name='flowstep',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flow_steps', to='contacts.Contact'),
        ),
        migrations.AddField(
            model_name='flowstep',
            name='messages',
            field=models.ManyToManyField(help_text='Any messages that are associated with this step (either sent or received)', related_name='steps', to='msgs.Msg'),
        ),
        migrations.AddField(
            model_name='flowstep',
            name='run',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='flows.FlowRun'),
        ),
        migrations.AddField(
            model_name='flowstart',
            name='contacts',
            field=models.ManyToManyField(help_text='Contacts that will start the flow', to='contacts.Contact'),
        ),
        migrations.AddField(
            model_name='flowstart',
            name='created_by',
            field=models.ForeignKey(help_text='The user which originally created this item', on_delete=django.db.models.deletion.CASCADE, related_name='flows_flowstart_creations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='flowstart',
            name='flow',
            field=models.ForeignKey(help_text='The flow that is being started', on_delete=django.db.models.deletion.CASCADE, related_name='starts', to='flows.Flow'),
        ),
        migrations.AddField(
            model_name='flowstart',
            name='groups',
            field=models.ManyToManyField(help_text='Groups that will start the flow', to='contacts.ContactGroup'),
        ),
        migrations.AddField(
            model_name='flowstart',
            name='modified_by',
            field=models.ForeignKey(help_text='The user which last modified this item', on_delete=django.db.models.deletion.CASCADE, related_name='flows_flowstart_modifications', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='flowruncount',
            name='flow',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='counts', to='flows.Flow'),
        ),
        migrations.AddField(
            model_name='flowrun',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='runs', to='contacts.Contact'),
        ),
        migrations.AddField(
            model_name='flowrun',
            name='flow',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='runs', to='flows.Flow'),
        ),
        migrations.AddField(
            model_name='flowrun',
            name='org',
            field=models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, related_name='runs', to='orgs.Org'),
        ),
        migrations.AddField(
            model_name='flowrun',
            name='parent',
            field=models.ForeignKey(help_text='The parent run that triggered us', null=True, on_delete=django.db.models.deletion.CASCADE, to='flows.FlowRun'),
        ),
        migrations.AddField(
            model_name='flowrun',
            name='session',
            field=models.ForeignKey(blank=True, help_text='The session that handled this flow run, only for voice flows', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='runs', to='channels.ChannelSession'),
        ),
        migrations.AddField(
            model_name='flowrun',
            name='start',
            field=models.ForeignKey(blank=True, help_text='The FlowStart objects that started this run', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='runs', to='flows.FlowStart'),
        ),
        migrations.AddField(
            model_name='flowrun',
            name='submitted_by',
            field=models.ForeignKey(help_text='The user which submitted this flow run', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='flowrevision',
            name='created_by',
            field=models.ForeignKey(help_text='The user which originally created this item', on_delete=django.db.models.deletion.CASCADE, related_name='flows_flowrevision_creations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='flowrevision',
            name='flow',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='revisions', to='flows.Flow'),
        ),
        migrations.AddField(
            model_name='flowrevision',
            name='modified_by',
            field=models.ForeignKey(help_text='The user which last modified this item', on_delete=django.db.models.deletion.CASCADE, related_name='flows_flowrevision_modifications', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='flowpathcount',
            name='flow',
            field=models.ForeignKey(help_text='The flow where the activity occurred', on_delete=django.db.models.deletion.CASCADE, related_name='activity', to='flows.Flow'),
        ),
        migrations.AddField(
            model_name='flowlabel',
            name='org',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orgs.Org'),
        ),
        migrations.AddField(
            model_name='flowlabel',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='flows.FlowLabel', verbose_name='Parent'),
        ),
        migrations.AddField(
            model_name='flow',
            name='created_by',
            field=models.ForeignKey(help_text='The user which originally created this item', on_delete=django.db.models.deletion.CASCADE, related_name='flows_flow_creations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='flow',
            name='labels',
            field=models.ManyToManyField(blank=True, help_text='Any labels on this flow', related_name='flows', to='flows.FlowLabel', verbose_name='Labels'),
        ),
        migrations.AddField(
            model_name='flow',
            name='modified_by',
            field=models.ForeignKey(help_text='The user which last modified this item', on_delete=django.db.models.deletion.CASCADE, related_name='flows_flow_modifications', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='flow',
            name='org',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flows', to='orgs.Org'),
        ),
        migrations.AddField(
            model_name='flow',
            name='saved_by',
            field=models.ForeignKey(help_text='The user which last saved this flow', on_delete=django.db.models.deletion.CASCADE, related_name='flow_saves', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='exportflowresultstask',
            name='created_by',
            field=models.ForeignKey(help_text='The user which originally created this item', on_delete=django.db.models.deletion.CASCADE, related_name='flows_exportflowresultstask_creations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='exportflowresultstask',
            name='flows',
            field=models.ManyToManyField(help_text='The flows to export', related_name='exports', to='flows.Flow'),
        ),
        migrations.AddField(
            model_name='exportflowresultstask',
            name='modified_by',
            field=models.ForeignKey(help_text='The user which last modified this item', on_delete=django.db.models.deletion.CASCADE, related_name='flows_exportflowresultstask_modifications', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='exportflowresultstask',
            name='org',
            field=models.ForeignKey(help_text='The Organization of the user.', on_delete=django.db.models.deletion.CASCADE, related_name='flow_results_exports', to='orgs.Org'),
        ),
        migrations.AddField(
            model_name='actionset',
            name='flow',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='action_sets', to='flows.Flow'),
        ),
        migrations.AddField(
            model_name='actionlog',
            name='run',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='flows.FlowRun'),
        ),
        migrations.AlterIndexTogether(
            name='flowstep',
            index_together=set([('step_uuid', 'next_uuid', 'rule_uuid', 'left_on')]),
        ),
        migrations.AlterIndexTogether(
            name='flowruncount',
            index_together=set([('flow', 'exit_type')]),
        ),
        migrations.AlterIndexTogether(
            name='flowpathcount',
            index_together=set([('flow', 'from_uuid', 'to_uuid', 'period')]),
        ),
        migrations.AlterUniqueTogether(
            name='flowlabel',
            unique_together=set([('name', 'parent', 'org')]),
        ),
    ]
