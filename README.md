# adventofcode2023
Back to python to brush up. Making conscious effort to not use AI, since it removes the fun from the game - Copilot disabled and only using general python references.

> Spoiler warning in the following daily commentaries

## Day 1: Trubuchet?!
Started easy, just removing all the non-digits from the string and taking the first and last. The second part was evil, it took me far too long to realise the overlapping nature of things like twone and eightwo and why string replacement wouldn't work, so I ended up scanning back and forth for matches instead, which ended up a little clumsy. I think this difficult start was a deliberate anti-AI effort, since figuring out the answer required some proper thinking. Edit: in hindsight, there was no need to scan backwards from the end, I could have just kept moving forward adding matches to a list.

## Day 2: Cube Conundrum
Back in the game, two very simple parts achievable with easy loops and string processing. Easy peasy, those elves have big hands.

## Day 3: Gear Ratios
Always enjoy the puzzles where you operate in 2D space. My boundary checking felt lazy, and the code could have been a lot cleaner in separate functions, but it's a Sunday morning and I'm still a bit sleepy. I knew when I was writing part-searching code in the first part that there would be a twist where parts would become secondary data and I'd end up with awful code for the second part. Took some time to learn how to use tuples in Python better though, I could rewrite the first part better with tuples, but again, it's Sunday morning :)

## Day 4: Scratchcards
Sets. lists and a while loop for an iterative approach to the solution, spent more time bug fixing boundary conditions.

## Day 5: If You Give A Seed A Fertilizer
Didn't pay attention to the size of the values in the puzzle input and wrote a naive solution which I completely regretted in part2 when discovering they were ranges, and that my loops would now iterate many billions of times. Skipped part2 for now, will return and write a version that performs boundary checking instead.

## Day 6: Wait For It
Went with another naive solution that was unusable in the second part. Didn't anticipate that twist with reading the input differently and had a solution that gobbled up all the memory. Half an hour spent re-learning the quadratic equation, and lots of paper scribbles later and a new solution devised for the second part.