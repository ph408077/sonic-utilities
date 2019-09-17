import click
from debug.main import AliasedGroup,cli
from debug.main import run_command

#
# This group houses Spanning_tree commands and subgroups
#
@cli.group(cls=AliasedGroup, default_if_no_args=False, invoke_without_command=True)
@click.pass_context
def spanning_tree(ctx):
    '''debug spanning_tree commands'''
    if ctx.invoked_subcommand is None:
        command = 'sudo stpctl dbg enable'
        run_command(command)
    pass

@spanning_tree.group('dump', cls=AliasedGroup, default_if_no_args=False, invoke_without_command=True)
def stp_debug_dump():
    pass

@stp_debug_dump.command('global')
def stp_debug_dump_global():
    command = 'sudo stpctl global'
    run_command(command)
    pass

@stp_debug_dump.command('vlan')
@click.argument('vlan_id', metavar='<vlan_id>', required=True)
def stp_debug_dump_vlan(vlan_id):
    command = 'sudo stpctl vlan ' + vlan_id
    run_command(command)
    pass

@stp_debug_dump.command('interface')
@click.argument('vlan_id', metavar='<vlan_id>', required=True)
@click.argument('interface_name', metavar='<interface_name>', required=True)
def stp_debug_dump_vlan_intf(vlan_id, interface_name):
    command = 'sudo stpctl port ' + vlan_id + " " + interface_name
    run_command(command)
    pass

@spanning_tree.command('show')
def stp_debug_show():
    command = 'sudo stpctl dbg show'
    run_command(command)
    pass

@spanning_tree.command('reset')
def stp_debug_reset():
    command = 'sudo stpctl dbg disable'
    run_command(command)
    pass

@spanning_tree.command('bpdu')
@click.argument('mode', metavar='{rx|tx}', required=False)
@click.option('-d', '--disable', is_flag=True)
def stp_debug_bpdu(mode, disable):
    if disable:
        if mode == 'rx':
            command = 'sudo stpctl dbg bpdu rx-off'
        elif mode == 'tx':
            command = 'sudo stpctl dbg bpdu tx-off'
        else:
            command = 'sudo stpctl dbg bpdu off'
    else:
        if mode == 'rx':
            command = 'sudo stpctl dbg bpdu rx-on'
        elif mode == 'tx':
            command = 'sudo stpctl dbg bpdu tx-on'
        else:
            command = 'sudo stpctl dbg bpdu on'
    run_command(command)
    pass

@spanning_tree.command('verbose')
@click.option('-d', '--disable', is_flag=True)
def stp_debug_verbose(disable):
    if disable:
        command = 'sudo stpctl dbg verbose off'
    else:
        command = 'sudo stpctl dbg verbose on'
    run_command(command)
    pass

@spanning_tree.command('event')
@click.option('-d', '--disable', is_flag=True)
def stp_debug_event(disable):
    if disable:
        command = 'sudo stpctl dbg event off'
    else:
        command = 'sudo stpctl dbg event on'
    run_command(command)
    pass

@spanning_tree.command('vlan')
@click.argument('vlan_id', metavar='<vlan_id/all>', required=True)
@click.option('-d', '--disable', is_flag=True)
def stp_debug_vlan(vlan_id, disable):
    if disable:
        command = 'sudo stpctl dbg vlan ' + vlan_id + ' off'
    else:
        command = 'sudo stpctl dbg vlan ' + vlan_id + ' on'
    run_command(command)
    pass

@spanning_tree.command('interface')
@click.argument('interface_name', metavar='<interface_name/all>', required=True)
@click.option('-d', '--disable', is_flag=True)
def stp_debug_intf(interface_name, disable):
    if disable:
        command = 'sudo stpctl dbg port ' + interface_name + ' off'
    else:
        command = 'sudo stpctl dbg port ' + interface_name + ' on'
    run_command(command)
    pass


