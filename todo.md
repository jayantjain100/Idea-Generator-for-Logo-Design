## Stuff that can be done


#### Resolved/Done

- Smart removal of a point
	- currently we remove a point that has minimal connextivity (Not exactly ideal )
	- choose the point that doesnt break current progress or something like that

- Instead of loops over all nPk perms, we can somehow smartly choose the candidates? (take inspiration from the data mining course?) ==> We chose to look at those subgraphs which were isomerphic

- A function prune which removes all edges which dont contribute to the final name/letter

- Let a drawing be defined by the position of some points - thats it. Then you wont have to check for lines etc, assume full connectivity. Just check length and angle constraints. Cause currently it might be the case that the points exist but a segment was missing and we are unable to get to the letter because of that. If we implement it without lines in the drawing, then, would it be slower? maybe not cause PnC is over points, we will not reject a set early on (by connectivity) since full connectivity will always be there. ===> Did this but it reduced interpretability

- profile code and see the bottlenecks ==> Profiled and optimised 
- does printing waste time? ==> Profiled and saw no (maybe recheck when display is off)

- Enforcing enclosed figures ==> Animesh said that this won't necessarily look good

- remove the point which doesnt appear in any letter or appears the least ==> Done by our removal strategy according to the num of "hits"

- concern - a letter with more points will take a long long time (even if the combinations are less, ther permutations grow crazily)
	- might not be a bad idea to look into the dfs idea
	- this would have already been done right
	- Graph tool directly gives this functionality to get all subgraphs of a given papa graph isomorphic to a given baby graph
	- use the networkx analogue pehle and then profile and see if its the slowest step or not
	- ===> Done

- is plotting along side wasting time? Yes

- can match against removed one level subgraphs and removed 2 level subgraphs to get a sense of direction
	- delta mei then a match against a 1 removed subgraph would also count
	- whats happening currently is that is tries to find a but it cant at all
	==> incorrect observation since code was wrong (I wasnt allowing connections between existing ppl)


#### Pending

- Smartly choosing the next transition 
	- looking at the contribution of adding an edge - maybe specifically looking at the combinations involving the new pt
	- having a continuous score function that guides us towards creating a letter
	- incentive to minimise the number of points and segments

- If a line segment cuts some one else, do we want to break it over there or not? ==> Couldnt decide yes or no

- later when we get many possible drawings for a name, we need to weigh the aesthetic value etc - are all letters the same size etc  
	- how would we guide using this aesthetic value


- Can add OR operations between letter interactions
	- currently the low high does not support all possibilities for letter "A"'s middle bar

- Need to reduce pruning time somehow, cause when we use -connect-collinear then it is really slow (unaffected by display) (remove useless lines?)

- if we use connect-collinear, do we want to alter the line drawing function to avoid one line highlighting more than the other

- flexible letter structure - optional segment  - easy way to implement is to have a function that takes in a letter and the points/lines to remove collectively and then does it 

- from letter description to design 

- add a print function in the letter which gives human readable text about the structure and all interactions/constraints

- delta jump for choosing the edge to add?

- since we are faster, think of increasing the degrees of freedom

- delta_step version gets stuck because it keeps on trying to fix one constraint which might be unfixable, and it doesn't explore

- support for floating point numbers to include all angles possible

- pruning not working properly? 
	- check in the generated images
	- with new_angles some constraints dont match cause of the 26.5 deg angle, this could be the reason

- add more letters

- sometimes a pt is removed that was crucial, why does this happen? bug?
	- add toughness wapas se?

- think if an A is even possible if I use new_jumps with base = [(2,1),(1,2)]