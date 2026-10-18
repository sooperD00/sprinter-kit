# A reading list for the person, and stops with modes

For `[h-616c5d]`, from a kit review on 2026-10-17. A draft, not a rule: nothing cites it.

## The claim

The person's reading time is the constraint. Agents run faster than the person can read, and
every stop so far is warranted. So the process keeps the person's reading on what only they
can judge, and makes what to read next obvious.

## The split

- The kit declares what the person reads at each agent step, as data in the repo.
- The console decides when and how to show it, and keeps the person's read and unread state.
  That state is personal, so it stays out of the repo.
- An agent can't make the person read. A prompt instruction decays, and a reminder in the
  transcript scrolls away. The nudge belongs in the console's UI.

## Stop modes

| Mode | Fits |
|------|------|
| Stop | decisions only the person owns: the planning decisions table, anything irreversible |
| Conditional | stops that check work: diff reviews, docs-pass fixes, a quiet planning level |
| Don't stop | pre-flight prints: the model line, the leg grep |

- A stop earns its mode by its record, the way acceptance sampling's switching rules move
  between normal, reduced and tightened inspection. A stop approved unchanged for many legs
  is a candidate for reduced. One change snaps it back to normal.
- The r- files already log what each stop changed. The reflect agent (`[s-b0557c]`) is the
  natural thing to count it.
- ADR-004's draft already holds one condition: a quiet level costs the person a line, not a
  stop.

## Console nudges (for sprint-runner)

| Nudge | Anchor | Why it works |
|-------|--------|--------------|
| A button that shows the right doc at the right time | Calm technology | Pull, not push. No badges, praise or achievements. |
| A quiz or summary from a doc | Retrieval practice | Recalling fixes it in memory better than rereading. |
| A "not read" bar | Buffer management | The unread pile is the buffer in front of the constraint. |
| Hold the next agent step while the bar is full | The rope, in drum-buffer-rope | An unread backlog becomes a stop condition. |

## Sketch: what the person reads while each agent step runs

Not how it runs today. A starting point for the reading list's format.

| Agent step | The person reads | Already exists as |
|------------|------------------|-------------------|
| prompt5, coding the leg | the files it will touch, to write the grok | the g- file |
| prompt6, EXPECT and COMPARE | the sprint's Decisions and Watches | the sprint file |
| prompt6, TEACH | (the person is the input here) | the l- file |
| prompt7, docs pass | the l- file's exercises | the l- template |
| prompt4, planning | the last leg's Landed note | the sprint file |

## Rows for the essay's lineage table

Add each row when the thing it names exists. The first two exist today.

| In the kit | Established practice | Source |
| --- | --- | --- |
| Agents stop themselves on an abnormal state (a dirty tree, zero or several legs handed off) | Jidoka (autonomation) | Toyota Production System (Taiichi Ohno) |
| The person's reading time is the constraint the process is built around | Theory of Constraints | Eliyahu Goldratt, *The Goal* (1984) |
| A reading list for the person, paired with each agent step | Standardized Work Combination Table | Toyota Production System |
| Stops that earn reduced inspection by their record | Switching rules, skip-lot sampling | MIL-STD-105E; ANSI/ASQ Z1.4 |

## References

- Eliyahu M. Goldratt and Jeff Cox, *The Goal* (1984): Theory of Constraints, drum-buffer-rope,
  buffer management.
- Taiichi Ohno, *Toyota Production System* (1978; English edition 1988): jidoka.
- Lean Enterprise Institute, *Lean Lexicon*: the Standardized Work Combination Table.
- MIL-STD-105E (1989), succeeded by ANSI/ASQ Z1.4: switching rules for normal, reduced and
  tightened inspection.
- Mark Weiser and John Seely Brown, "Designing Calm Technology" (1995) and "The Coming Age of
  Calm Technology" (1996), Xerox PARC.
- Henry L. Roediger III and Jeffrey D. Karpicke, "Test-Enhanced Learning: Taking Memory Tests
  Improves Long-Term Retention," *Psychological Science* (2006): retrieval practice.
