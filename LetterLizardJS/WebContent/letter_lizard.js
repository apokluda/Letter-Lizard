// REPORT: when assigned to in the functions below without the var keyword
// these become properties of the global object
//var stage;
//var queue;
//var scramble;

// REPORT: using closure to encapsulate private data
function getTileFactory(scramble) {
	
	var spriteSheet = new createjs.SpriteSheet({
		images: [queue.getResult("letters")],
		frames: [[0,   158, 42, 42], // A
		         [43,  158, 35, 42], // B
		         [78,  158, 34, 42], // C
		         [112, 158, 37, 42], // D
		         [149, 158, 28, 42], // E
		         [177, 158, 28, 42], // F
		         [205, 158, 39, 42], // G
		         [244, 158, 35, 42], // H 
		         [279, 158, 18, 42], // I
		         [297, 158, 26, 42], // J
		         [323, 158, 39, 42], // K 
		         [362, 158, 28, 42], // L
		         [0,   210, 54, 42], // M
		         [54,  210, 38, 42], // N
		         [92,  210, 42, 42], // O
		         [134, 210, 32, 42], // P
		         [166, 210, 44, 42], // Q
		         [210, 210, 38, 42], // R
		         [248, 210, 33, 42], // S
		         [281, 210, 30, 42], // T
		         [311, 210, 37, 42], // U
		         [348, 210, 41, 42], // V
		         [0,   260, 50, 42], // W
		         [50,  260, 42, 42], // X
		         [96,  260, 37, 42], // Y
		         [133, 260, 38, 42], // Z
		]});
	
	var offsets = [{x:2,  y:2}, // A
	               {x:6,  y:3}, // B
	               {x:6,  y:3}, // C
	               {x:6,  y:3}, // D
	               {x:10, y:3}, // E
	               {x:10, y:3}, // F
	               {x:4,  y:4}, // G
	               {x:6,  y:4}, // H
	               {x:15, y:4}, // I
	               {x:10, y:3}, // J
	               {x:5,  y:3}, // K
	               {x:10, y:3}, // L
	               {x:-3, y:2}, // M
	               {x:5,  y:3}, // N
	               {x:3,  y:4}, // O
	               {x:10, y:3}, // P
	               {x:3,  y:4}, // Q
	               {x:5,  y:3}, // R
	               {x:7,  y:3}, // S
	               {x:9,  y:3}, // T
	               {x:6,  y:3}, // U
	               {x:5,  y:3}, // V
	               {x:0,  y:3}, // W
	               {x:4,  y:3}, // X
	               {x:6,  y:3}, // Y
	               {x:5,  y:2}, // Z
	               ];
	
	return function(letter) {
		var index = letter.charCodeAt(0) - 65;
		var sprite = new createjs.Sprite(spriteSheet);
		sprite.gotoAndStop(index);
		sprite.setTransform(offsets[index].x, offsets[index].y);
		
		var g = new createjs.Graphics();
		g.beginStroke("#000000").beginFill("#FFFFFF").drawRoundRect(0, 0, 50, 50, 5);
		var s = new createjs.Shape(g);
		
		// REPORT: adding property to function
		var tile = new Tile(letter);
		tile.container = new createjs.Container();
		tile.container.addChild(s);
		tile.container.addChild(sprite);
		return tile;
	};
}

function Tile(letter) {
	this.letter = letter;
	this.saved = {};
}

Tile.prototype = {
	placeAt: function(x, y) {
		this.container.x = x;
		this.container.y = y;
	},
	
	moveTo: function(x, y) {
		// Moves the tile to the specified x and y coordinates.
		// This function is called by the Scramble and Builder classes
		createjs.Tween.get(this.container).to({x:x, y:y}, 500);
	},
	
	saveLocation: function() {
		this.saved.x = this.container.x;
		this.saved.y = this.container.y;
	},
	
	reset: function() {
		moveToXY(this.saved.x, this.saved.y);
	},
};

// REPORT: Object oriented design using prototypes
function Scramble(letters, x, y, w) {
	this.letters = letters;
	// We store the tiles in an array instead of a dictionary becasue
	// there may be duplicate letters
	this.tiles = [];
	this.x = x;
	this.y = y;
	
	var g = new createjs.Graphics();
	g.beginStroke("#000000").drawRoundRect(0, 0, w, 70, 5);
	var s = new createjs.Shape(g);
	s.x = this.x;
	s.y = this.y;
	stage.addChild(s);

	// Create a tile for each letter in the scramble and place them
	// in their proper position in the row
	var tileFactory = getTileFactory(this);
	for (var i = 0; i < letters.length; ++i) {
		var letter = letters.charAt(i);
		var tile = tileFactory(letter);
		tile.placeAt(this.x + 10 + 60 * i, this.y + 10);
		tile.saveLocation();
		tile.scramblePos = i;
		stage.addChild(tile.container);
		this.tiles[i] = tile;
	}
}

// An implementation of the Fisher-Yates shuffle
//+ Jonas Raoni Soares Silva
//@ http://jsfromhell.com/array/shuffle [v1.0]
shuffle = function(o){ //v1.0
	for(var j, x, i = o.length; i; j = parseInt(Math.random() * i), x = o[--i], o[i] = o[j], o[j] = x);
	return o;
};

Scramble.prototype = {
	getTile: function(letter) {
		// Get the first tile that contains the letter for keyCode
		// if it exists has has not been given to the Builder
		for (var i = 0; i < this.tiles.length; ++i) {
			if (this.tiles[i] && this.tiles[i].letter == letter) {
				var tile = this.tiles[i];
				this.tiles[i] = undefined;
				return tile;
			}
		}
	},
	
	returnTile: function(tile) {
		// Causes the tile to be returned to its original position
		// in the scramble
		this.tiles[tile.scramblePos] = tile;
		tile.reset();
	},

	shuffle: function() {
		// Changes the order of the letters
		this.tiles = shuffle(this.tiles);
		for (var i = 0; i < this.tiles.length; ++i) {
			var tile = this.tiles[i];
			tile.moveTo(this.x + 10 + 60 * i, this.y + 10);
			tile.saveLocation();
			tile.scramblePos = i;
		}
	}
};

function Builder(scramble) {
	this.scramble = scramble;
}

Builder.prototype = {
	takeTile: function(letter) {
		// Moves the tile
		var tile = scramble.getTile(letter);
		if (tile) {
			tile.moveTo();
		}
	},

	getWord: function() {
		// Return the word formed by the tiles placed in the Builder
	},
	
	reset: function() {
		// for tile in tiles, tile.reset();
	}
};

function init() {
	stage = new createjs.Stage("llcanvas");
	
	loadingTxt = new createjs.Text("Loading...", "bold 24px Arial");
	loadingTxt.textAlign = "center";
	loadingTxt.x = stage.canvas.width / 2;
	loadingTxt.y = stage.canvas.height / 2;
	
	stage.addChild(loadingTxt);
	stage.update();
	
	queue = new createjs.LoadQueue();
	// REPORT: inline function / closure
	queue.addEventListener("progress",
		function (event) {
			loadingTxt.text = "Loading... " + (queue.progress*100|0) + "%";
			stage.update();
	}
	);
	queue.addEventListener("complete", loadComplete);
	queue.loadManifest([{id:"title", src:"assets/letter_lizard.png"},
	                    {id:"lizard", src:"assets/lizard.png"},
	                    {id:"letters", src:"assets/letters.png"}]);
}

var sprites = {};

function loadComplete(event) {
	stage.removeAllChildren();		// clear the loading message
	
	var cw = stage.canvas.width;	// The width of the canvas
	var ch = stage.canvas.height;	// The height of the canvas
	var lx = cw * 0.70;				// The x-coord of the start of the word list
	
	var bmp = new createjs.Bitmap(queue.getResult("title"));
	bmp.x = (cw - lx) / 2;
	bmp.y = 0;
	stage.addChild(bmp);
	
	var bmp = new createjs.Bitmap(queue.getResult("lizard"));
	bmp.setTransform(0, ch - bmp.image.height*0.8, 0.8, 0.8);
	stage.addChild(bmp);
	
	var g = new createjs.Graphics();
	g.beginFill("#000000").rect(0, 15, 2, ch - 30);
	var divider = new createjs.Shape(g);
	divider.x = lx;
	divider.y = 0;
	stage.addChild(divider);
	
	scramble = new Scramble("ABCDEF", 50, 140, lx - 100);
	
	createjs.Ticker.setFPS(30);
	createjs.Ticker.addEventListener("tick", tick);
	
	placeDOMElements();
	
	var bShuffle = document.getElementById("btn:shuffle");
	bShuffle.onclick = function() {
		scramble.shuffle();
	}
	document.onkeydown = handleKeyDown;
	window.onresize = placeDOMElements;
}

function placeDOMElements() {
	var cx = stage.canvas.offsetLeft;
	var cy = stage.canvas.offsetTop;
	
	var bMainMenu = document.getElementById("btn:mainMenu");
	bMainMenu.style.left = (cx + 250) + "px";
	bMainMenu.style.top = (cy + 500) + "px";
	bMainMenu.style.display = "inline";
	
	var bHint = document.getElementById("btn:hint");
	bHint.style.width = bMainMenu.offsetWidth + "px";
	bHint.style.left = (cx + 260 + bMainMenu.offsetWidth) + "px";
	bHint.style.top = (cy + 500) + "px";
	bHint.style.display = "inline";
	
	var bShuffle = document.getElementById("btn:shuffle");
	bShuffle.style.width = bMainMenu.offsetWidth + "px";
	bShuffle.style.left = (cx + 270 + 2*bMainMenu.offsetWidth) + "px";
	bShuffle.style.top = (cy + 500) + "px";
	bShuffle.style.display = "inline";
}

function tick(event) {
	stage.update();
	console.log("updated stage");
}

function handleKeyDown(e) {
	// cross browser issues exist
	if (!e) { e = window.event; }
	switch (e.keyCode)
	{
	case 65: // A
	case 32: // spacebar
		scramble.shuffle();
	}
}