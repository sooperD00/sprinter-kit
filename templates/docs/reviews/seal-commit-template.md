# Seal commit template

A seal commit closes one review block: the review of one row of a leg's Commits table. Its message says what the review found and what changed because of it, for an engineer who was not there. A later session can read a leg's seals in order and see what planning keeps leaving out.

- Make it when the block's review file is closed and the tree is clean.
- It changes no files: `git commit --allow-empty -F <message file>`.
- Take the subject and the section labels from this file as they are, so one search finds every seal and one script can split them.

## Subject

    review(<sprint-id>-<leg>.<block>): seal <block name>

| Part | Is |
|------|----|
| `<sprint-id>-<leg>` | the leg, as in `[s-9cf8b9-c]`, without `[s-` and `]` |
| `<block>` | the row's number in the leg's Commits table |
| `<block name>` | the row's name |

Example: `review(9cf8b9-c.2): seal order totals`

Read one leg's seals, oldest first:

    git log --reverse --format='%B' --grep='^review(9cf8b9-c\.[0-9]*): seal '

Read every seal on a branch:

    git log main..HEAD --reverse --format='%B' --grep='^review([^)]*): seal '

- Don't search for `^review` alone. It also finds every commit whose subject starts `review:`, and every commit with a body line that starts with `review`, because `^` matches at the start of any line of the message.
- `main..HEAD` is empty on `main` itself. There, select by the leg in the pattern.

## Body

    Scope: <the files reviewed, and the leg. What each file defines. Every
    model, field and term the summary goes on to name, explained once.>

    The review found <N> problems. <All N are fixed. | Which are not, and
    where they went.>
    1. <One problem, in one sentence.>
    2. <...>

    Spec changes (<file>):
    - <What the spec says now.> <An example value.>

    Code changes (<directory>):
    - <Who changed what.> Before, <what the code did>.
    - <The validator> now rejects each of these, which it accepted before:
      - <One case, with an example value.>

    Test changes (<directory>):
    The suite had <A> tests before the review and has <B> now.
    - <What the new tests assert, with examples.>
    - Final check. <What was run at the end, and what it showed.>

    Other doc changes:
    - <file>: <what it gained, and what a reader gets from it>.

    Filed for later, not done:
    - <file>: <what was filed, and what it asks for>.

    Review-file: <path of the block's review file>
    Review-range: <first commit of the block>^..<last commit before the seal>

- Keep each label on its own line, spelled as above and ending in a colon. Leave out a section with nothing in it.
- Start no line with `#`. Git deletes those lines when a message is saved from an editor, which `git commit --amend` and a rebase's `reword` both do.
- Wrap at 78 columns. Don't break a line inside backticks.
- The last two lines are git trailers. Keep them in the last paragraph, with any `Co-Authored-By` line. `git log -1 --format='%(trailers:key=Review-range,valueonly)'` reads one back, and `git log <Review-range>` lists the block's commits.

## Writing rules

Write for an engineer who knows the language and the tools, and has not seen this code or this review.

1. Start from what was reviewed. Say what each file defines before saying what was wrong with it.
2. Name the thing every time: the model, the field, the file. Not "the record", "the check" or "it".
3. Explain a term where it first appears: "`status` is one of five values, among them `open` and `paid`".
4. Say what the code did and what it does now, with values. Not "accepted nonsense" but "accepted `quantity: 0`". Not "is stricter" but "rejects `quantity` of 0 or less".
5. Give code no feelings or motives. Code is never trusting, confused, fooled or happy.
6. Give every sentence an actor and an active verb: "the reviewer planted", "we moved", "the validator rejects". Not "was rejected" or "loaded without complaint".
7. For each code change, say what happened before it.
8. Give an example value for each rule.
9. Give counts, and take each from a command run now: tests before and after, defects planted, statements and branches covered.
10. Leave out the review's own item numbers and turn numbers. The `Review-file` trailer leads to them.
11. Keep "filed" apart from "done". A filed item is open work: say where it was filed and what it asks for.
12. List changes in the order of the sections: spec, code, tests, other docs, filed.

## Where the facts come from

- The block's review file: what the review found, each decision, each expected result and each answer. It also gives the test count from before the review.
- `git log --reverse --format='%h %s' <first commit of the block>^..HEAD`: what changed, in order.
- The test suite, run now: the count after the review.
- `housekeeping.md`, `techdebt.md` and the sprint file: what was filed, and what is still open.

Check each number by running the command it comes from. Don't copy one from an earlier message.
