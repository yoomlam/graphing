# graphing

![My graph](https://g.gravizo.com/source/custom_mark1?https%3A%2F%2Fraw.githubusercontent.com%2Fyoomlam%2Fgraphing%2Fmaster%2FREADME.md)

<details> 
<summary>Hi</summary>
custom_mark1
  digraph G {
    size ="4,4";
    main [shape=box];
    main -> parse [weight=8];
    parse -> execute;
    main -> init [style=dotted];
    main -> cleanup;
    execute -> { make_string; printf};
    init -> make_string;
    edge [color=red];
    main -> printf [style=bold,label="100 times"];
    make_string [label="make a string"];
    node [shape=box,style=filled,color=".7 .3 1.0"];
    execute -> compare;
  }
custom_mark1
</details>


![Sample graph](https://g.gravizo.com/source/custom_mark10?https%3A%2F%2Fraw.githubusercontent.com%2FTLmaK0%2Fgravizo%2Fmaster%2FREADME.md)

