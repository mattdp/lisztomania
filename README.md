## Goal

Use a simple command to generate a to-do list of routines for the day, which:
* is pastable into emacs
* allows me to do only the essentials on busy days, with a more expansive routine when I have more time
* incorporates randomness to keep things interesting

## How to use

```
./composer.py -p <priority: ["red"|"yellow"|"green"]> -d <daytype: ["workday"|"weekend"]>
```

Output is written to "todays_routine.org", consumable by emacs org-mode. Sample file included in this repo.
Change quotes.csv to modify which quotes appear in your routine.
Change elements.csv to modify which elements are included in your routines on red (challenging), yellow (normal), green (lots of free time) days, and what's part of your work life vs. your personal life.

## Completed features

* Morning/afternoon/evening classification
* In-code arg for how many * at base
* Add enough to CSV that it can be tested
* Uptake CSV into hashes in python
* Output the whole thing, in emacs format, to terminal
* Output to a saved file that overwrites
* CLI input, but no output changes, for 1) life or life+work 2) priority
* Output changes in results using CLI
* Outfit for AM routine and use for 3 days
