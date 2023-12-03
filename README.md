# adventofcode2023
Back to python to brush up. Making conscious effort to not use AI, since it removes the fun from the game - Copilot disabled and only using general python references.

> Spoiler warning in the following daily commentaries

## Day 1
Started easy, just removing all the non-digits from the string and taking the first and last. The second part was evil, it took me far too long to realise the overlapping nature of things like twone and eightwo and why string replacement wouldn't work, so I ended up scanning back and forth for matches instead, which ended up a little clumsy. I think this difficult start was a deliberate anti-AI effort, since figuring out the answer required some proper thinking.

## Day 2
Back in the game, two very simple parts achievable with easy loops and string processing. Easy peasy, those elves have big hands.

## Day 3
Always enjoy the puzzles where you operate in 2D space. My boundary checking felt lazy, and the code could have been a lot cleaner in separate functions, but it's a Sunday morning and I'm still a bit sleepy. I knew when I was writing part-searching code in the first part that there would be a twist where parts would become secondary data and I'd end up with awful code for the second part. Took some time to learn how to use tuples in Python better though, I could rewrite the first part better with tuples, but again, it's Sunday morning :)