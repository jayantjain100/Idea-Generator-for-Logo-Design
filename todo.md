### Stuff that can be done

- Smartly choosing the next transition 
	- looking at the contribution of adding an edge - maybe specifically looking at the combinations involving the new pt
	- having a continuous score function that guides us towards creating a letter
	- incentive to minimise the number of points and segments

- Smart removal of a point
	- currently we remove a point that has minimal connextivity (Not exactly ideal )
	- choose the point that doesnt break current progress or something like that

- Instead of loops over all nPk perms, we can somehow smartly choose the candidates? (take inspiration from the data mining course?)

- If a line segment cuts some one else, do we want to break it over there or not?

- A function prune which removes all edges which dont contribute to the final name/letter

- Let a drawing be defined by the position of some points - thats it. Then you wont have to check for lines etc, assume full connectivity. Just check length and angle constraints. Cause currently it might be the case that the points exist but a segment was missing and we are unable to get to the letter because of that. If we implement it without lines in the drawing, then, would it be slower? maybe not cause PnC is over points, we will not reject a set early on (by connectivity) since full connectivity will always be there. 

- later when we get many possible drawings for a name, we need to weigh the aesthetic value etc - are all letters the same size etc  

- profile code and see the bottlenecks

- does printing waste time?

- Enforcing enclosed figures, removing un-needed line segments in the end, 

- remove the point which doesnt appear in any letter or appears the least

- add more letters

- concern - a letter with more points will take a long long time (even if the combinations are less, ther permutations grow crazily)
	- might not be a bad idea to look into the dfs idea
	- this would have already been done right
	- Graph tool directly gives this functionality to get all subgraphs of a given papa graph isomorphic to a given baby graph
	- use the networkx analogue pehle and then profile and see if its the slowest step or not

- is plotting along side wasting time?

- Can add OR operations between letter interactions
	- currently the low high does not support all possibilities for letter "A"'s middle bar

	
