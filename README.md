# graphing

![My graph](https://g.gravizo.com/source/custom_mark12?https%3A%2F%2Fraw.githubusercontent.com%2Fyoomlam%2Fgraphing%2Fmaster%2FREADME.md)
<details> 
<summary>Hi</summary>
custom_mark12
  digraph G {
    size ="4,4";
    main [shape=box];
    main -> parser [weight=8];
  }
custom_mark12
</details>

![Alt text](https://g.gravizo.com/svg?digraph%20G%20%7B%0A%20%20%20%20size%20%3D%224%2C4%22%3B%0A%20%20%20%20main%20%5Bshape%3Dbox%5D%3B%0A%20%20%20%20main%20-%3E%20parse%20%5Bweight%3D8%5D%3B%0A%20%20%7D)

![Alt text](https://g.gravizo.com/source/custom_mark13?https%3A%2F%2Fraw.githubusercontent.com%2Fyoomlam%2Fgraphing%2Fmaster%2FREADME.md)
<details> 
<summary></summary>
custom_mark13
/**
*Structural Things
*@opt commentname
*@note Notes can
*be extended to
*span multiple lines
*/
class Structural{}

/**
*@opt all
*@note Class
*/
class Counter extends Structural {
        static public int counter;
        public int getCounter();
}

/**
*@opt shape activeclass
*@opt all
*@note Active Class
*/
class RunningCounter extends Counter{}
custom_mark13
</details>


![Alt text](https://g.gravizo.com/source/custom_svg?https%3A%2F%2Fraw.githubusercontent.com%2Fyoomlam%2Fgraphing%2Fmaster%2FREADME.md)
<details> 
<summary></summary>
custom_svg
@gravizosvg
{"svg": {
		"@height": "450",
		"@width": "450", 
		"path": [
			{"@id":"lineAB", "@d": "M 100 350 l 150 -300", "@stroke":"red"},
			{"@id":"lineBC", "@d": "M 250 50 l 150 300", "@stroke":"red"},
			{"@d":"M 100 350 q 150 -300 300 0", "@stroke":"green", "@fill":"none"}
    ],
		"g": [
			{"@stroke":"black", "circle":[  
				{"@id":"pointA", "@cx":"100", "@cy":"350", "@r":"3"},
				{"@id":"pointB", "@cx":"250", "@cy":"50", "@r":"3"},
				{"@id":"pointC", "@cx":"400", "@cy":"350", "@r":"3"}
			]},
			{"text": [
				{"@x":"100", "@y":"350", "@dx":"-30", "$":"A"},
				{"@x":"250", "@y":"50", "@dy":"-10", "$":"B"},
				{"@x":"400", "@y":"350", "@dx":"30", "$":"C"}
			]}
		]
	}
}
custom_svg
</details>
