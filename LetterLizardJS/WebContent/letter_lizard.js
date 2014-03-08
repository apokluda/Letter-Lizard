var stage;
var queue;

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

function Scramble(letters) {
	this.letters = letters;
	
	// Create a tile for each letter in the scramble and place them
	// in their proper position in the row
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
	
	var g = new createjs.Graphics();
	g.beginFill("#000000").rect(0, 15, 3, ch - 30);
	var divider = new createjs.Shape(g);
	divider.x = lx;
	divider.y = 0;
	stage.addChild(divider);
	
	var spriteSheet = new createjs.SpriteSheet({
		images: [queue.getResult("letters")],
		frames: [[0, 160, 42, 50, 0]]
	});
	spriteA = new createjs.Sprite(spriteSheet, 0);
	spriteA.setTransform(2, 2);
	var container = new createjs.Container();
	container.addChild(spriteA);
	
	var g = new createjs.Graphics();
	g.beginStroke("#000000").drawRoundRect(0, 0, 50, 50, 5);
	var s = new createjs.Shape(g);
	container.addChild(s);
	
	container.x = 100;
	container.y = 100;
	
	sprites.A = container;
	createjs.Tween.get(container).to({x:500}, 1000);
	
	createjs.Ticker.setFPS(30);
	createjs.Ticker.addEventListener("tick", tick);
	
	stage.addChild(container);
	
	document.onkeydown = handleKeyDown;
}

function tick(event) {
	stage.update();
	console.log("updated stage");
}

function handleKeyDown(e) {
	// cross browser issues exist
	if (!e) { e = window.event; }
	if (e.keyCode == 65) {
		console.log("Moving A. keyCode = " + e.keyCode);
		createjs.Tween.get(sprites.A).to({y:800}, 1000);
	}
}