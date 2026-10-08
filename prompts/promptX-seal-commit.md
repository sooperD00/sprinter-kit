Write the seal commit for review block <n> of [s-<id>-<leg>]: <block name>.

- Review file: `docs/sprints/reviews/r-<id>-<leg>-<short-description>.md`
- Follow `~/repos/sprinter-kit/templates/docs/reviews/seal-commit-template.md`:
  its subject, its section labels, its trailers and its writing rules.
- Take the facts from the review file and from `git log <first>^..HEAD`. Run
  the suite, and any other command a number comes from.
- The reader is an engineer who has not seen this code or this review.
- Show me the message first. Commit it, empty, when I say so.
