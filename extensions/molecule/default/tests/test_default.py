import re

def test_mfecma_is_installed(host):
    mfecma = host.package("mfecma")
    assert mfecma.is_installed
    assert mfecma.version.startswith("5.8.5"), "Le paquet Trellix Agent (mfecma) devrait être installé"

def test_mfedx_is_installed(host):
    mfedx = host.package("mfedx")
    assert mfedx.is_installed
    assert mfedx.version.startswith("6.0.3"), "Le paquet Trellix Data Exchange Layer (mfedx) devrait être installé"

def test_mcafeeesp_is_installed(host):
    mcafeeesp = host.package("mcafeeesp")
    assert mcafeeesp.is_installed
    assert mcafeeesp.version.startswith("10.7.21"), "Le paquet Trellix Endpoint Security Platform for Linux (mcafeeesp) devrait être installé"

def test_mcafeeespaac_is_installed(host):
    mcafeeespaac = host.package("mcafeeespaac")
    assert mcafeeespaac.is_installed
    assert mcafeeespaac.version.startswith("10.7.21"), "Le paquet Trellix Endpoint Security Platform Arbitrary Access Control (mcafeeespaac) devrait être installé"

def test_mcafeeespfileaccess_is_installed(host):
    mcafeeespfileaccess = host.package("mcafeeespfileaccess")
    assert mcafeeespfileaccess.is_installed
    assert mcafeeespfileaccess.version.startswith("10.7.21"), "Le paquet Trellix Endpoint Security Platform File Access for Linux (mcafeeespfileaccess) devrait être installé"

def test_mcafeert_is_installed(host):
    mcafeert = host.package("mcafeert")
    assert mcafeert.is_installed
    assert mcafeert.version.startswith("10.7.21"), "Le paquet Trellix Runtime for Linux (mcafeert) devrait être installé"

def test_mcafeetp_is_installed(host):
    mcafeetp = host.package("mcafeetp")
    assert mcafeetp.is_installed
    assert mcafeetp.version.startswith("10.7.21"), "Le paquet Trellix Endpoint Security for Linux Threat Prevention (mcafeetp) devrait être installé"

def test_mcafeefw_is_installed(host):
    mcafeefw = host.package("mcafeefw")
    assert mcafeefw.is_installed
    assert mcafeefw.version.startswith("10.7.21"), "Le paquet Trellix Endpoint Security for Linux Firewall (mcafeefw) devrait être installé"

def test_msgbus_communication(host):
    cmd = host.run("/opt/McAfee/agent/bin/cmdagent -i")
    assert cmd.rc == 0
    assert re.search(r"Status: Enabled", cmd.stdout), "L'agent Trellix devrait être opérationnelle"

def test_msgbus_communication(host):
    cmd = host.run("/opt/McAfee/agent/bin/cmdagent -i")
    assert cmd.rc == 0
    assert re.search(r"TA msgbus communication: OK", cmd.stdout), "La communication msgbus avec l'agent Trellix devrait être opérationnelle"

def test_ens_getapstatus(host):
    cmd = host.run("/opt/McAfee/ens/tp/bin/mfetpcli --getapstatus")
    assert cmd.rc == 0
    assert re.search(r"Access Protection: Enabled", cmd.stdout), "Le statut de la protection d'accès devrait être activé"

def test_ens_getepstatus(host):
    cmd = host.run("/opt/McAfee/ens/tp/bin/mfetpcli --getepstatus")
    assert cmd.rc == 0
    assert re.search(r"Exploit Prevention: Enabled", cmd.stdout), "Le statut de la protection d'exploit devrait être activé"

def test_ens_getspstatus(host):
    cmd = host.run("/opt/McAfee/ens/tp/bin/mfetpcli --getspstatus")
    assert cmd.rc == 0
    assert re.search(r"Self Protection: Enabled", cmd.stdout), "Le statut de la self protection devrait être activé"

def test_ens_getfwstatus(host):
    cmd = host.run("/opt/McAfee/ens/fw/bin/mfefwcli --fw status")
    assert cmd.rc == 0
    assert re.search(r"Status: Enabled", cmd.stdout), "Le statut du pare-feu devrait être activé"
