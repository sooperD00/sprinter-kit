# Field guide

Domain terms a reviewer may not know, how they relate, and where they bite.

<!-- HOW TO ADD AN ENTRY
Keep this comment. People read the field guide for its terms, and agents read the raw file, so
the rules for adding an entry live here.

The test: could a strong engineer with no background in this domain tell whether a line of code
is right? If not, and what's missing is domain knowledge rather than code knowledge, it's an
entry.

Look for:
- numbers and limits with a domain reason
- orders and conventions that come from a standard or a data source (axis order, units, ID
  formats)
- deliberate omissions that look like bugs
- domain names and acronyms in identifiers, docstrings and comments
- standards cited with no explanation

Skip language and library mechanics, which are code knowledge. Why the project chose one thing
over another belongs in design.md or a decision record.

Group entries under an area named with the standard or source it follows: `## Dates (ISO 8601)`.
Under the heading, "Used by:" names the modules that rely on it. Lead each entry with a bold
claim, then explain it.

Point code at the area once per module, from the highest docstring that covers it:
`(See docs/field-guide.md#dates-iso-8601.)` GitHub builds the anchor from the heading: lower
case, punctuation dropped, spaces as hyphens.
-->

## An area, named with the standard or source it follows

Used by: the modules that rely on it

**A claim about a term.** What it means, and where it bites.
