import textwrap

from magic import decklist


def test_parse() -> None:
    s = """
        3 Barter in Blood
        4 Consume Spirit
        4 Demonic Rising
        4 Devour Flesh
        2 Distress
        2 Dread Statuary
        4 Haunted Plate Mail
        3 Homicidal Seclusion
        4 Hymn to Tourach
        2 Infest
        4 Quicksand
        4 Spawning Pool
        14 Swamp
        2 Ultimate Price
        4 Underworld Connections

        Sideboard
        1 Distress
        2 Dystopia
        1 Infest
        4 Memoricide
        2 Nature's Ruin
        1 Pharika's Cure
        4 Scrabbling Claws"""
    s = textwrap.dedent(s)
    d = decklist.parse(s)
    assert sum(d['maindeck'].values()) == 60
    assert len(d['maindeck']) == 15
    assert len(d['sideboard']) == 7


def test_parse2() -> None:
    s = """
        3 Barter in Blood
        4 Consume Spirit
        4 Demonic Rising
        4 Devour Flesh
        2 Distress
        2 Dread Statuary

        4 Haunted Plate Mail
        3 Homicidal Seclusion
        4 Hymn to Tourach
        2 Infest

        4 Quicksand
        4 Spawning Pool
        14 Swamp
        2 Ultimate Price
        4 Underworld Connections

        1 Distress
        2 Dystopia
        1 Infest
        4 Memoricide
        2 Nature's Ruin
        1 Pharika's Cure
        4 Scrabbling Claws"""
    s = textwrap.dedent(s)
    d = decklist.parse(s)
    assert len(d['maindeck']) == 15
    assert len(d['sideboard']) == 7


def test_parse3() -> None:
    s = """
        3 Barter in Blood
        4 Consume Spirit
        4 Demonic Rising
        4 Devour Flesh
        2 Distress
        2 Dread Statuary
        4 Haunted Plate Mail
        3 Homicidal Seclusion
        4 Hymn to Tourach
        2 Infest
        4 Quicksand
        4 Spawning Pool
        14 Swamp
        2 Ultimate Price
        4 Underworld Connections

        1 Distress
        2 Dystopia
        1 Infest
        4 Memoricide
        2 Nature's Ruin
        1 Pharika's Cure
        4 Scrabbling Claws"""
    s = textwrap.dedent(s)
    d = decklist.parse(s)
    assert len(d['maindeck']) == 15
    assert len(d['sideboard']) == 7

def test_parse4() -> None:
    s = """








        3 Barter in Blood
        4 Consume Spirit
        4 Demonic Rising
        4 Devour Flesh
        2 Distress
        2 Dread Statuary
        4 Haunted Plate Mail
        3 Homicidal Seclusion
        4 Hymn to Tourach
        2 Infest
        4 Quicksand
        4 Spawning Pool
        14 Swamp
        2 Ultimate Price
        4 Underworld Connections

        Sideboard
        1 Distress
        2 Dystopia
        1 Infest
        4 Memoricide
        2 Nature's Ruin
        1 Pharika's Cure
        4 Scrabbling Claws





    """
    s = textwrap.dedent(s)
    d = decklist.parse(s)
    assert len(d['maindeck']) == 15
    assert len(d['sideboard']) == 7

def test_parse5() -> None:
    s = """
        4 Animist's Awakening
        4 Copperhorn Scout
        14 Forest
        4 Harvest Season
        4 Jaddi Offshoot
        4 Krosan Wayfarer
        4 Loam Dryad
        4 Nantuko Monastery
        4 Nest Invader
        4 Quest for Renewal
        4 Rofellos, Llanowar Emissary
        2 Sky Skiff
        4 Throne of the God-Pharaoh

        0 Villainous Wealth
    """
    s = textwrap.dedent(s)
    d = decklist.parse(s)
    assert len(d['maindeck']) == 13
    assert len(d['sideboard']) == 1

# Test that a 71 card deck includes the last 15 as sideboard
def test_parse6() -> None:
    s = """
        4 Animist's Awakening
        4 Copperhorn Scout
        15 Forest
        4 Harvest Season
        4 Jaddi Offshoot
        4 Krosan Wayfarer
        4 Loam Dryad
        4 Nantuko Monastery
        4 Nest Invader
        4 Quest for Renewal
        4 Rofellos, Llanowar Emissary
        2 Sky Skiff
        4 Throne of the God-Pharaoh
        1 Distress
        2 Dystopia
        1 Infest
        4 Memoricide
        2 Nature's Ruin
        1 Pharika's Cure
        4 Scrabbling Claws
    """
    s = textwrap.dedent(s)
    d = decklist.parse(s)
    assert sum(d['maindeck'].values()) == 61
    assert len(d['maindeck']) == 13
    assert len(d['sideboard']) == 7

# Test a 63 card deck + 12 sideboard
def test_parse7() -> None:
    s = """
        16 Forest
        4 Animist's Awakening
        4 Copperhorn Scout
        4 Harvest Season
        4 Jaddi Offshoot
        4 Krosan Wayfarer
        4 Loam Dryad
        4 Nantuko Monastery
        4 Nest Invader
        4 Quest for Renewal
        4 Rofellos, Llanowar Emissary
        4 Sky Skiff
        4 Dystopia
        1 Infest
        4 Memoricide
        2 Nature's Ruin
        1 Pharika's Cure
        4 Scrabbling Claws
    """
    s = textwrap.dedent(s)
    d = decklist.parse(s)
    assert sum(d['maindeck'].values()) == 64
    assert sum(d['sideboard'].values()) == 12
    assert len(d['maindeck']) == 13
    assert len(d['sideboard']) == 5

# Test a 61 card deck + 15 sideboard with one-offs around the cut
def test_parse8() -> None:
    s = """
        24 Island
        4 Curious Homunculus
        4 Prism Ring
        4 Anticipate
        4 Take Inventory
        4 Dissolve
        3 Void Shatter
        3 Jace's Sanctum
        3 Whelming Wave
        2 Control Magic
        2 Confirm Suspicions
        2 Counterbore
        1 Rise from the Tides
        1 Cryptic Serpent
        1 Convolute
        1 Lone Revenant
        1 Careful Consideration
        1 Opportunity
        4 Annul
        4 Invasive Surgery
        3 Sentinel Totem
    """
    s = textwrap.dedent(s)
    d = decklist.parse(s)
    assert sum(d['maindeck'].values()) == 61
    assert sum(d['sideboard'].values()) == 15
    assert d['maindeck']['Cryptic Serpent'] == 1
    assert d['sideboard']['Convolute'] == 1

# Test a Gatherling deck with no sideboard
def test_parse9() -> None:
    s = """
        2 Bonded Horncrest
        4 Boros Guildgate
        2 Charging Monstrosaur
        2 Frenzied Raptor
        3 Imperial Lancer
        8 Mountain
        2 Nest Robber
        2 Pious Interdiction
        9 Plains
        1 Pterodon Knight
        2 Rallying Roar
        2 Shining Aerosaur
        3 Sky Terror
        2 Slash of Talons
        4 Stone Quarry
        2 Sure Strike
        2 Swashbuckling
        3 Territorial Hammerskull
        2 Thrash of Raptors
        1 Tilonalli's Skinshifter
        2 Unfriendly Fire

        Sideboard"""
    s = textwrap.dedent(s)
    d = decklist.parse(s)
    assert sum(d['maindeck'].values()) == 60
    assert sum(d['sideboard'].values()) == 0
    assert d['maindeck']['Shining Aerosaur'] == 2

def test_parse10() -> None:
    s = """
        Sideboard"""
    s = textwrap.dedent(s)
    d = decklist.parse(s)
    assert sum(d['maindeck'].values()) == 0
    assert sum(d['sideboard'].values()) == 0

# Test a Commander deck.
def test_parse11() -> None:
    s = """
        1 Groundskeeper
        1 Jaddi Offshoot
        1 Scute Mob
        1 Frontier Guide
        1 Llanowar Scout
        1 Grazing Gladehart
        1 Mwonvuli Beast Tracker
        1 Ranging Raptors
        1 Embodiment of Fury
        1 Grove Rumbler
        1 Mina and Denn, Wildborn
        1 Cultivator of Blades
        1 Embodiment of Insight
        1 Garruk's Packleader
        1 Akoum Hellkite
        1 Baloth Woodcrasher
        1 Oran-Rief Hydra
        1 Rubblehulk
        1 Borborygmos
        1 Skarrg Goliath
        1 Myojin of Infinite Rage
        1 Apocalypse Hydra
        1 Lay of the Land
        1 Blackblade Reforged
        1 Broken Bond
        1 Evolution Charm
        1 Fork in the Road
        1 Ground Assault
        1 Rampant Growth
        1 Signal the Clans
        1 Deep Reconnaissance
        1 Elemental Bond
        1 Fires of Yavimaya
        1 Grow from the Ashes
        1 Hammer of Purphoros
        1 Harrow
        1 Journey of Discovery
        1 Nissa's Pilgrimage
        1 Retreat to Valakut
        1 Ghirapur Orrery
        1 Seek the Horizon
        1 Seer's Sundial
        1 Splendid Reclamation
        1 Overwhelming Stampede
        1 Rude Awakening
        1 Nissa's Renewal
        1 Animist's Awakening
        1 Clan Defiance
        1 Blighted Woodland
        1 Evolving Wilds
        16 Forest
        1 Gruul Guildgate
        1 Kazandu Refuge
        14 Mountain
        1 Mountain Valley
        1 Rogue's Passage
        1 Rugged Highlands
        1 Sylvan Ranger
        1 Vinelasher Kudzu
        1 Viridian Emissary
        1 Zhur-Taa Druid
        1 Tunneling Geopede
        1 World Shaper
        1 Zendikar Incarnate
        1 Verdant Force
        1 Strata Scythe
        1 Sylvan Awakening
        1 The Mending of Dominaria
        1 Zendikar's Roil
        1 Sunbird's Invocation
        1 Zendikar Resurgent
        1 Timber Gorge
        """
    s = textwrap.dedent(s)
    d = decklist.parse(s)
    assert sum(d['maindeck'].values()) == 100
    assert sum(d['sideboard'].values()) == 0
    assert d['maindeck']['Timber Gorge'] == 1