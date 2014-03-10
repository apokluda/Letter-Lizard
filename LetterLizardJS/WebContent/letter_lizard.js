var stage;
var queue;
var tiles = {};

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
		         [311,], // U
		         [], // V
		         [], // W
		         [], // X
		         [], // Y
		         [], // Z
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
	               {}, // U
	               {}, // V
	               {}, // W
	               {}, // X
	               {}, // Y
	               {}, // Z
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
		var tile = new Tile(letter, scramble);
		tile.container = new createjs.Container();
		tile.container.addChild(s);
		tile.container.addChild(sprite);
		return tile;
	};
}

function Tile(letter, scramble) {
	this.letter = letter;
	this.scramble = scramble;
}

Tile.prototype = {
	moveTo: function(x, y) {
		// Moves the tile to the specified x and y coordinates.
		// This function is called by the Scramble and Builder classes
	},
	
	reset: function() {
		this.scramble.returnTile(this);
	}
};

// REPORT: Object oriented design using prototypes
function Scramble(letters, x, y, w) {
	this.letters = letters;
	
	// Create a tile for each letter in the scramble and place them
	// in their proper position in the row
	var g = new createjs.Graphics();
	g.beginStroke("#000000").drawRoundRect(0, 0, w, 70, 5);
	var s = new createjs.Shape(g);
	s.x = x;
	s.y = y;
	stage.addChild(s);

	var tileFactory = getTileFactory(this);
//	var tile = tileFactory("A");
//	tile.scramblePos = 0;
//	
//	tile.container.x = 60;
//	tile.container.y = 150;
//	stage.addChild(tile.container);
//	
//	var tile = tileFactory("B");
//	tile.scramblePos = 1;
//	
//	tile.container.x = 60 * (tile.scramblePos + 1);
//	tile.container.y = 150;
//	stage.addChild(tile.container);
//	
	var tile = tileFactory("C");
	tile.scramblePos = 3;
	
	tile.container.x = 60 * (tile.scramblePos + 1);
	tile.container.y = 150;
	stage.addChild(tile.container);
	tiles.C = tile;
//	
//	var tile = tileFactory("D");
//	tile.scramblePos = 3;
//	
//	tile.container.x = 60 * (tile.scramblePos + 1);
//	tile.container.y = 150;
//	stage.addChild(tile.container);
//	
//	var tile = tileFactory("E");
//	tile.scramblePos = 4;
//	
//	tile.container.x = 60 * (tile.scramblePos + 1);
//	tile.container.y = 150;
//	stage.addChild(tile.container);
//	
//	var tile = tileFactory("F");
//	tile.scramblePos = 5;
//	
//	tile.container.x = 60 * (tile.scramblePos + 1);
//	tile.container.y = 150;
//	stage.addChild(tile.container);
//	
//	var tile = tileFactory("G");
//	tile.scramblePos = 6;
//	
//	tile.container.x = 60 * (tile.scramblePos + 1);
//	tile.container.y = 150;
//	stage.addChild(tile.container);
//	
//	var tile = tileFactory("H");
//	tile.scramblePos = 7;
//	
//	tile.container.x = 60 * (tile.scramblePos + 1);
//	tile.container.y = 150;
//	stage.addChild(tile.container);
//	
	var tile = tileFactory("I");
	tile.scramblePos = 2;
	
	tile.container.x = 60 * (tile.scramblePos + 1);
	tile.container.y = 150;
	stage.addChild(tile.container);
	tiles.I = tile;
//	
//	var tile = tileFactory("J");
//	tile.scramblePos = 9;
//	
//	tile.container.x = 60 * (tile.scramblePos + 1);
//	tile.container.y = 150;
//	stage.addChild(tile.container);
//	
//	var tile = tileFactory("K");
//	tile.scramblePos = 0;
//	
//	tile.container.x = 60 * (tile.scramblePos + 1);
//	tile.container.y = 150;
//	stage.addChild(tile.container);
//	
//	var tile = tileFactory("L");
//	tile.scramblePos = 1;
//	
//	tile.container.x = 60 * (tile.scramblePos + 1);
//	tile.container.y = 150;
//	stage.addChild(tile.container);
//	
//	var tile = tileFactory("M");
//	tile.scramblePos = 2;
//	
//	tile.container.x = 60 * (tile.scramblePos + 1);
//	tile.container.y = 150;
//	stage.addChild(tile.container);
//	
//	var tile = tileFactory("N");
//	tile.scramblePos = 3;
//	
//	tile.container.x = 60 * (tile.scramblePos + 1);
//	tile.container.y = 150;
//	stage.addChild(tile.container);
//	
//	var tile = tileFactory("O");
//	tile.scramblePos = 4;
//	
//	tile.container.x = 60 * (tile.scramblePos + 1);
//	tile.container.y = 150;
//	stage.addChild(tile.container);
//	
	var tile = tileFactory("P");
	tile.scramblePos = 1;
	
	tile.container.x = 60 * (tile.scramblePos + 1);
	tile.container.y = 150;
	stage.addChild(tile.container);
	tiles.P = tile;
//	
//	var tile = tileFactory("Q");
//	tile.scramblePos = 6;
//	
//	tile.container.x = 60 * (tile.scramblePos + 1);
//	tile.container.y = 150;
//	stage.addChild(tile.container);
//	
	var tile = tileFactory("R");
	tile.scramblePos = 0;
	
	tile.container.x = 60 * (tile.scramblePos + 1);
	tile.container.y = 150;
	stage.addChild(tile.container);
	tiles.R = tile;
	
	var tile = tileFactory("S");
	tile.scramblePos = 5;
	
	tile.container.x = 60 * (tile.scramblePos + 1);
	tile.container.y = 150;
	stage.addChild(tile.container);
	tiles.S = tile;
	
	var tile = tileFactory("T");
	tile.scramblePos = 4;
	
	tile.container.x = 60 * (tile.scramblePos + 1);
	tile.container.y = 150;
	stage.addChild(tile.container);
	tiles.T = tile;
}

Scramble.prototype = {
	getTile: function(keyCode) {
		// Get the first tile that contains the letter for keyCode
		// if it exists has has not been given to the Builder
	},
	
	returnTile: function(tile) {
		// Causes the tile to be returned to its original position
		// in the scramble
	},

	scramble: function() {
		// Changes the order of the letters
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
	
	var scramble = new Scramble("A", 50, 140, lx - 100);
	
	createjs.Ticker.setFPS(30);
	createjs.Ticker.addEventListener("tick", tick);
	
	placeDOMElements();
	
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
	case 83:
		createjs.Tween.get(tiles.S.container).to({x:60, y:250}, 500);
		break;
	case 67:
		createjs.Tween.get(tiles.C.container).to({x:120, y:250}, 500);
		break;
	case 82:
		createjs.Tween.get(tiles.R.container).to({x:180, y:250}, 500);
		break;
	case 73:
		createjs.Tween.get(tiles.I.container).to({x:240, y:250}, 500);
		break;
	case 80:
		createjs.Tween.get(tiles.P.container).to({x:300, y:250}, 500);
		break;
	case 84:
		createjs.Tween.get(tiles.T.container).to({x:360, y:250}, 500);
		break;
	}
}