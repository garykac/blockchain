# Spell fragment card data

# Text -> ASCII Art: http://patorjk.com/software/taag/#p=display&f=Rectangles&t=Monster

# Data Format:
#   spell_card_data:
#     List of <pattern-info>
#
#   <pattern-info>:
#     <pattern>, List of <card>s that use pattern
#
#   <card>:
#     <title>, <attributes>, List of <description> strings
#
#   <attribute>:
#     'element'

# Spell patterns are normalized:
#  * If spell has '@', then it should be in upper-left corner
#    * If not possible, then in top row as close as possible to upper-left corner
#      * If multiple options, then choose option with '.' in upper-left
#  * Else 'X' in upper-left corner. 
#  * Prefer wider spells over taller spells.

# Element properties
# ==================
#
# Air
#  * Opposed to Earth
#  * Properties: masculine, active, light (weight), bright, thin
#      movement, travel, flying, finding, teaching, imagination, sound
#  * Primary Ability: Physical movement
#  * Secondary Abilities:
#  * Tendrils: manipulate
#
# Fire
#  * Opposed to Water
#  * Properties: masculine, active, light (weight), bright, thin
#      movement, transformation, change, destruction, hot
#  * Primary Ability: Attack
#  * Secondary Abilities:
#  * Tendrils: quick, many, temporary, attack
#
# Earth
#  * Opposed to Air
#  * Properties: feminine, passive, heavy, dark, thick
#      stability, quiet, birth, fertility, strength, cool, solid
#  * Primary Ability: Defense, Stability
#  * Secondary Abilities:
#  * Tendrils: slow, safe, stable, anchored
#
# Water
#  * Opposed to Fire
#  * Properties: feminine, passive, heavy, dark, thick
#      motion, flowing, living, cleansing, psychic, scrying/mirrors, dreams, cool
#  * Primary Ability: Astral Movement
#  * Secondary Abilities:
#  * Tendrils: quick, few, stable

spell_card_data = [

	#  _____         _           _    ___   
	# |   | |___ _ _| |_ ___ ___| |  |_  |  
	# | | | | -_| | |  _|  _| .'| |   _| |_ 
	# |_|___|___|___|_| |_| |__,|_|  |_____|
	#

	# +---+
	# | X |  Level 0
	# +---+
	[	[	"X",
		],
		[	["Creep",
				{'element': 'none'},
				["Move a TENDRIL one space in any direction."] ],
		],
	],

	#  _____         _           _    ___ 
	# |   | |___ _ _| |_ ___ ___| |  |_  |
	# | | | | -_| | |  _|  _| .'| |  |  _|
	# |_|___|___|___|_| |_| |__,|_|  |___|
	#

	# +-----+
	# | X X |  Level 1
	# +-----+
	[	[	"X X",
		],
		[],
	],

	# +-----+
	# | X . |  Level 1
	# | . X |
	# +-----+
	[	[	"X .",
			". X",
		],
		[],
	],

	# +-------+
	# | X . X |  Level 1
	# +-------+
	[	[	"X . X",
		],
		[],
	],

	# +-------+
	# | X . . |  Level 1
	# | . . X |
	# +-------+
	[	[	"X . .",
			". . X",
		],
		[	["Teleport Back",
				{'element': 'none'},
				["When on the Astral Plane, follow a TENDRIL back to the Physical Realm."] ],
		],
	],

	# +-------+
	# | X . . |  Level 2
	# | . . . |
	# | . . X |
	# +-------+
	[	[	"X . .",
			". . .",
			". . X",
		],
		[],
	],

	# +---------+
	# | X . . X |  Level 2
	# +---------+
	[	[	"X . . X",
		],
		[],
	],

	# +---------+
	# | X . . . |  Level 2
	# | . . . X |
	# +---------+
	[	[	"X . . .",
			". . . X",
		],
		[],
	],

	# +---------+
	# | X . . . |  Level 2
	# | . . . . |
	# | . . . X |
	# +---------+
	[	[	"X . . .",
			". . . .",
			". . . X",
		],
		[],
	],

	#  _____         _           _    ___ 
	# |   | |___ _ _| |_ ___ ___| |  |_  |
	# | | | | -_| | |  _|  _| .'| |  |_  |
	# |_|___|___|___|_| |_| |__,|_|  |___|
	#

	# +-------+
	# | X X X |  Level 2
	# +-------+
	[	[	"X X X",
		],
		[],
	],

	# +-------+
	# | X X . |  Level 2
	# | . . X |
	# +-------+
	[	[	"X X .",
			". . X",
		],
		[],
	],

	# +-----+
	# | X X |  Level 2
	# | . X |
	# +-----+
	[	[	"X X",
			". X",
		],
		[],
	],

	# +-------+
	# | X . X |  Level 2
	# | . X . |
	# +-------+
	[	[	"X . X",
			". X .",
		],
		[],
	],

	# +-------+
	# | X . . |  Level 3
	# | . X . |
	# | . . X |
	# +-------+
	[	[	"X . .",
			". X .",
			". . X",
		],
		[],
	],

	#  _____ _                   _       _    ___        _      ___   
	# |   __| |___ _____ ___ ___| |_ ___| |  |_  |     _| |_   |_  |  
	# |   __| | -_|     | -_|   |  _| .'| |   _| |_   |_   _|   _| |_ 
	# |_____|_|___|_|_|_|___|_|_|_| |__,|_|  |_____|    |_|    |_____|
	#

	# +-----+
	# | @ X |  Level 1
	# +-----+
	[	[	"@ X",
		],
		[	["Haste",
				{'element': 'air'},
				["Gain 3 MP to use this turn:", "* 1MP to move into Field", "* 2MP to move into Forest", "* 3MP to move into Mountain"] ],
			["Protection",
				{'element': 'earth'},
				["Place 1 charge on this spell.", "Spend a charge at any time to protect against 1 attack."] ],
		],
	],

	# +-----+
	# | @ . |  Level 1
	# | . X |
	# +-----+
	[	[	"@ .",
			". X",
		],
		[	["Haste 2",
				{'element': 'air'},
				["Gain 5 MP to use this turn:", "* 1MP to move into Field", "* 2MP to move into Forest", "* 3MP to move into Mountain"] ],
			["Fire Burst",
				{'element': 'fire'},
				["Attack all creatures in a single location for 1pt damage."] ],
			["Teleport Away",
				{'element': 'water'},
				["Move self to Astral Plane."] ],
		],
	],

	# +-------+
	# | @ . X |  Level 1
	# +-------+
	[	[	"@ . X",
		],
		[	["Haste 3",
				{'element': 'air'},
				["Gain 5 MP to use this turn:", "* 1MP to move into Field", "* 2MP to move into Forest", "* 3MP to move into Mountain"] ],
		],
	],

	# +-------+
	# | @ . . |  Level 1
	# | . . X |
	# +-------+
	[	[	"@ . .",
			". . X",
		],
		[],
	],

	# +-------+
	# | @ . . |  Level 2
	# | . . . |
	# | . . X |
	# +-------+
	[	[	"@ . .",
			". . .",
			". . X",
		],
		[],
	],

	# +---------+
	# | @ . . X |  Level 2
	# +---------+
	[	[	"@ . . X",
		],
		[],
	],

	# +---------+
	# | @ . . . |  Level 2
	# | . . . X |
	# +---------+
	[	[	"@ . . .",
			". . . X",
		],
		[],
	],

	# +---------+
	# | @ . . . |  Level 2
	# | . . . . |
	# | . . . X |
	# +---------+
	[	[	"@ . . .",
			". . . .",
			". . . X",
		],
		[],
	],

	#  _____ _                   _       _    ___        _      ___ 
	# |   __| |___ _____ ___ ___| |_ ___| |  |_  |     _| |_   |_  |
	# |   __| | -_|     | -_|   |  _| .'| |   _| |_   |_   _|  |  _|
	# |_____|_|___|_|_|_|___|_|_|_| |__,|_|  |_____|    |_|    |___|
	#

	# +-------+                     +-----+     +-------+
	# | @ X X |  Level 2 - Built on | @ X | and | @ . X |
	# +-------+                     +-----+     +-------+
	[	[	"@ X X",
		],
		[],
	],

	# +-------+                     +-----+
	# | X @ X |  Level 2 - Built on | @ X |
	# +-------+                     +-----+
	[	[	"X @ X",
		],
		[],
	],

	# +-------+                     +-----+     +-------+
	# | @ . . |  Level 2 - Built on | @ . | and | @ . . |
	# | . X X |                     | . X |     | . . X |
	# +-------+                     +-----+     +-------+
	[	[	"@ . .",
			". X X",
		],
		[],
	],

	# +-------+                     +-----+     +-----+
	# | . @ X |  Level 2 - Built on | @ X | and | @ . | 
	# | X . . |                     +-----+     | . X |
	# +-------+                                 +-----+
	[	[	". @ X",
			"X . .",
		],
		[],
	],

	# +-------+                     +-----+     +-------+
	# | @ X . |  Level 2 - Built on | @ X | and | @ . . |
	# | . . X |                     +-----+     | . . X |
	# +-------+                                 +-------+
	[	[	"@ X .",
			". . X",
		],
		[],
	],

	# +-----+                     +-----+     +-----+
	# | @ . |  Level 2 - Built on | @ X | and | @ . |
	# | X X |                     +-----+     | . X |
	# +-----+                                 +-----+
	[	[	"@ .",
			"X X",
		],
		[],
	],

	# +-----+                     +-----+
	# | @ X |  Level 2 - Built on | @ X |
	# | X . |                     +-----+
	# +-----+
	[	[	"@ X",
			"X .",
		],
		[	["Split",
				{'element': 'earth'},
				["Place a new TENDRIL in the same location where you already have a TENDRIL."] ],
		],
	],

	# +-------+                     +-----+
	# | . @ . |  Level 2 - Built on | @ . |
	# | X . X |                     | . X |
	# +-------+                     +-----+
	[	[	". @ .",
			"X . X",
		],
		[],
	],

	# +-------+                     +-----+     +-------+
	# | @ . X |  Level 2 - Built on | @ . | and | @ . X |
	# | . X . |                     | . X |     +-------+
	# +-------+                     +-----+
	[	[	"@ . X",
			". X .",
		],
		[],
	],

	# +-------+                     +-----+     +-------+
	# | @ . . |  Level 3 - Built on | @ . | and | @ . . |
	# | . X . |                     | . X |     | . . . |
	# | . . X |                     +-----+     | . . X |
	# +-------+                                 +-------+
	[	[	"@ . .",
			". X .",
			". . X",
		],
		[],
	],

	# +-------+                     +-----+
	# | X . . |  Level 3 - Built on | @ . |
	# | . @ . |                     | . X |
	# | . . X |                     +-----+
	# +-------+
	[	[	"X . .",
			". @ .",
			". . X",
		],
		[	["Levitate",
				{'element': 'air'},
				["Place up to 3 charges on this spell", "Spend a charge to make all terraian cost 1MP for this turn"] ],
		],
	],

	# +---------+                     +-----+     +---------+
	# | @ X . X |  Level 3 - Built on | @ X | and | @ . . X |
	# +---------+                     +-----+     +---------+
	[	[	"@ X . X",
		],
		[],
	],

	# +---------+                     +-------+     +---------+
	# | @ . X X |  Level 3 - Built on | @ . X | and | @ . . X |
	# +---------+                     +-------+     +---------+
	[	[	"@ . X X",
		],
		[],
	],

	# +---------+                     +-----+     +-------+
	# | X @ . X |  Level 3 - Built on | @ X | and | @ . X |
	# +---------+                     +-----+     +-------+
	[	[	"X @ . X",
		],
		[],
	],

	# +---------+                     +-------+     +---------+
	# | @ . . . |  Level 3 - Built on | @ . . | and | @ . . . |
	# | . . X X |                     | . . X |     | . . . X |
	# +---------+                     +-------+     +---------+
	[	[	"@ . . .",
			". . X X",
		],
		[],
	],

	# +---------+                     +-----+     +-------+
	# | X @ . . |  Level 3 - Built on | @ X | and | @ . . |
	# | . . . X |                     +-----+     | . . X |
	# +---------+                                 +-------+
	[	[	"X @ . .",
			". . . X",
		],
		[],
	],

	# +---------+                     +-----+     +---------+
	# | @ X . . |  Level 3 - Built on | @ X | and | @ . . . |
	# | . . . X |                     +-----+     | . . . X |
	# +---------+                                 +---------+
	[	[	"@ X . .",
			". . . X",
		],
		[],
	],

	# +---------+                     +-----+     +---------+
	# | @ . . . |  Level 3 - Built on | @ . | and | @ . . . |
	# | . X . X |                     | . X |     | . . . X |
	# +---------+                     +-----+     +---------+
	[	[	"@ . . .",
			". X . X",
		],
		[],
	],

	# +---------+                     +-----+     +-------+
	# | . @ . X |  Level 3 - Built on | @ . | and | @ . X |
	# | X . . . |                     | . X |     +-------+
	# +---------+                     +-----+
	[	[	". @ . X",
			"X . . .",
		],
		[],
	],

	# +---------+                     +-------+     +---------+
	# | @ . X . |  Level 3 - Built on | @ . X | and | @ . . . |
	# | . . . X |                     +-------+     | . . . X |
	# +---------+                                   +---------+
	[	[	"@ . X .",
			". . . X",
		],
		[],
	],

	# +-------+                     +-----+     +-------+
	# | @ . X |  Level 2 - Built on | @ X | and | @ . X |
	# | X . . |                     +-----+     +-------+
	# +-------+
	[	[	"@ . X",
			"X . .",
		],
		[],
	],

	# +-------+                     +-----+     +-------+
	# | @ . . |  Level 2 - Built on | @ X | and | @ . . |
	# | X . X |                     +-----+     | . . X |
	# +-------+                                 +-------+
	[	[	"@ . .",
			"X . X",
		],
		[],
	],

	# +-------+                     +-------+     +-------+
	# | @ . X |  Level 2 - Built on | @ . X | and | @ . . |
	# | . . X |                     +-------+     | . . X |
	# +-------+                                   +-------+
	[	[	"@ . X",
			". . X",
		],
		[],
	],

	# +---------+                     +-------+     +---------+
	# | @ . . X |  Level 3 - Built on | @ . . | and | @ . . X |
	# | . . X . |                     | . . X |     +---------+
	# +---------+                     +-------+
	[	[	"@ . . X",
			". . X .",
		],
		[],
	],

	# +---------+                     +-----+     +-------+
	# | . @ . . |  Level 3 - Built on | @ . | and | @ . . |
	# | X . . X |                     | . X |     | . . X |
	# +---------+                     +-----+     +-------+
	[	[	". @ . .",
			"X . . X",
		],
		[],
	],

	# +---------+                     +-----+     +---------+
	# | @ . . X |  Level 3 - Built on | @ . | and | @ . . X |
	# | . X . . |                     | . X |     +---------+
	# +---------+                     +-----+
	[	[	"@ . . X",
			". X . .",
		],
		[],
	],

	# +---------+                     +-------+     +---------+
	# | @ . . . |  Level 3 - Built on | @ . . | and | @ . . . |
	# | . . X . |                     | . . X |     | . . . . |
	# | . . . X |                     +-------+     | . . . X |
	# +---------+                                   +---------+
	[	[	"@ . . .",
			". . X .",
			". . . X",
		],
		[],
	],

	# +---------+                     +-----+     +---------=
	# | @ . . . |  Level 3 - Build on | @ . | and | @ . . . |
	# | . X . . |                     | . X |     | . . . . |
	# | . . . X |                     +-----+     | . . . X |
	# +---------+                                 +---------+
	[	[	"@ . . .",
			". X . .",
			". . . X",
		],
		[],
	],

	# +---------+                     +-----+     +-------+
	# | X . . . |  Level 3 - Built on | @ . | and | @ . . |
	# | . @ . . |                     | . X |     | . . X |
	# | . . . X |                     +-----+     +-------+
	# +---------+
	[	[	"X . . .",
			". @ . .",
			". . . X",
		],
		[],
	],

	# +-------+                     +-------+
	# | . @ . |  Level 3 - Built on | @ . . |
	# | . . . |                     | . . X |
	# | X . X |                     +-------+
	# +-------+
	[	[	". @ .",
			". . .",
			"X . X",
		],
		[],
	],

	# +-----------+                     +-------+
	# | X . @ . X |  Level 3 - Built on | @ . X |
	# +-----------+                     +-------+
	[	[	"X . @ . X",
		],
		[],
	],

	# +-----------+                     +-------+     +-------+
	# | X . @ . . |  Level 3 - Built on | @ . X | and | @ . . |
	# | . . . . X |                     +-------+     | . . X |
	# +-----------+                                   +-------+
	[	[	"X . @ . .",
			". . . . X",
		],
		[],
	],

	# +-----------+                     +-------+     +-----------+
	# | @ . X . . |  Level 3 - Built on | @ . X | and | @ . . . . |
	# | . . . . X |                     +-------+     | . . . . X |
	# +-----------+                                   +-----------+
	[	[	"@ . X . .",
			". . . . X",
		],
		[],
	],

	# +-----------+                     +-------+     +-----------+
	# | @ . . . . |  Level 3 - Built on | @ . . | and | @ . . . . |
	# | . . X . X |                     | . . X |     | . . . . X |
	# +-----------+                     +-------+     +-----------+
	[	[	"@ . . . .",
			". . X . X",
		],
		[],
	],

	# +-----------+                     +-------+
	# | . . @ . . |  Level 3 - Built on | @ . . |
	# | X . . . X |                     | . . X |
	# +-----------+                     +-------+
	[	[	". . @ . .",
			"X . . . X",
		],
		[],
	],

	# +-----------+                     +-------+     +-----------+
	# | @ . . . X |  Level 3 - Built on | @ . . | and | @ . . . X |
	# | . . X . . |                     | . . X |     +-----------+
	# +-----------+                     +-------+
	[	[	"@ . . . X",
			". . X . .",
		],
		[],
	],

	# +-----------+                     +-------+
	# | X . . . . |  Level 3 - Built on | @ . . |
	# | . . @ . . |                     | . . X |
	# | . . . . X |                     +-------+
	# +-----------+
	[	[	"X . . . .",
			". . @ . .",
			". . . . X",
		],
		[],
	],

	# +-----------+                     +-------+     +-----------+
	# | @ . . . . |  Level 3 - Built on | @ . . | and | @ . . . . |
	# | . . X . . |                     | . . X |     | . . . . . |
	# | . . . . X |                     +-------+     | . . . . X |
	# +-----------+                                   +-----------+
	[	[	"@ . . . .",
			". . X . .",
			". . . . X",
		],
		[],
	],

	#  _____ _                   _       _    ___        _      ___ 
	# |   __| |___ _____ ___ ___| |_ ___| |  |_  |     _| |_   |_  |
	# |   __| | -_|     | -_|   |  _| .'| |   _| |_   |_   _|  |_  |
	# |_____|_|___|_|_|_|___|_|_|_| |__,|_|  |_____|    |_|    |___|
	#

	# +-------+                     +-----+     +-------+
	# | @ . X |  Level 4 - Built on | @ . | and | @ . X |
	# | . X . |                     | . X |     +-------+
	# | X . . |                     +-----+
	# +-------+
	[	[	"@ . X",
			". X .",
			"X . .",
		],
		[],
	],

	# +-------+                     +-----+     +-------+
	# | @ X . |  Level 4 - Build on | @ X | and | @ . . |
	# | X . . |                     +-----+     | . . . |
	# | . . X |                                 | . . X |
	# +-------+                                 +-------+
	[	[	"@ X .",
			"X . .",
			". . X",
		],
		[],
	],

	# +-------+                     +-------+     +-------+
	# | @ . X |  Level 4 - Build on | @ . X | and | @ . . |
	# | . . . |                     +-------+     | . . . |
	# | X . X |                                   | . . X |
	# +-------+                                   +-------+
	[	[	"@ . X",
			". . .",
			"X . X",
		],
		[],
	],

	#  _____ _                   _       _    ___      _      ___   
	# |   __| |___ _____ ___ ___| |_ ___| |  |_  |   _| |_   |_  |  
	# |   __| | -_|     | -_|   |  _| .'| |  |  _|  |_   _|   _| |_ 
	# |_____|_|___|_|_|_|___|_|_|_| |__,|_|  |___|    |_|    |_____|
	#

	# +-------+                     +-----+     +-------+
	# | @ @ X |  Level 2 - Built on | @ X | and | @ . X |
	# +-------+                     +-----+     +-------+
	[	[	"@ @ X",
		],
		[],
	],

	# +-------+                     +-----+
	# | @ X @ |  Level 2 - Built on | @ X |
	# +-------+                     +-----+
	[	[	"@ X @",
		],
		[],
	],

	# +-----+                     +-----+
	# | @ X |  Level 2 - Built on | @ X |
	# | . @ |                     +-----+
	# +-----+
	[	[	"@ X",
			". @",
		],
		[],
	],

	# +-----------+                     +-------+
	# | @ . . . . |  Level 3 - Built on | @ . . |
	# | . . X . . |                     | . . X |
	# | . . . . @ |                     +-------+
	# +-----------+
	[	[	"@ . . . .",
			". . X . .",
			". . . . @",
		],
		[],
	],

	#  _____ _                   _       _    ___      _      ___ 
	# |   __| |___ _____ ___ ___| |_ ___| |  |_  |   _| |_   |_  |
	# |   __| | -_|     | -_|   |  _| .'| |  |  _|  |_   _|  |  _|
	# |_____|_|___|_|_|_|___|_|_|_| |__,|_|  |___|    |_|    |___|
	#

	# +-----+                     +-----+
	# | @ X |  Level 3 - Built on | @ X |
	# | X @ |                     +-----+
	# +-----+
	[	[	"@ X",
			"X @",
		],
		[],
	],

	# +-------+                     +-----+
	# | . @ . |  Level 3 - Built on | @ . |
	# | X . X |                     | . X |
	# | . @ . |                     +-----+
	# +-------+
	[	[	". @ .",
			"X . X",
			". @ .",
		],
		[],
	],

]
