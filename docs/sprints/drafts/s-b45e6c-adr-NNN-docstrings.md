docs/DEVLOG/learn/l-faab97-a-foundation-dossier.md:365
### What gets a coding agent to write good docstrings: the prompt, an ADR, or the review?

All three, each for the part it can judge.

Parts:
1. A recipe -> an ADR or in the kit handbook
2. Trigger(s) -> reminder at the right time, or at the end
	- in the sprint template's done when (at the end)
	- e.g. "each module this leg adds or reshapes has a docstring according to ADR [docstring ADR]"
3. Comparisons that land for me: this is personal, could be a config if sprinter-kit
	had additional users. For now, add a one line in the ADR bc the agent can't guess
	my reference points. Me: SQL, a spreadsheet, the fab
4. Did it orient the reader? Human answers in the `g-` file. Exercise: read the docstring alone, write one sentence on what you expect the file to do, then read the file. If your sentence was wrong, the docstring failed, whoever wrote it.

ADR Draft: (also add the parts table and qeustion above, bc the reasoning is
important. Put it as a draft, and have the coding agent of sprinter-kit concentrate
on this when it's time to do so.)

```markdown
A module docstring orients a reader who has not opened the file.

- Line 1 names what the file is, and the spec section it carries.
- Then say what the file builds, in the order a reader meets it. Use a short numbered list when there are three parts or more.
- Say why a part exists when its name doesn't say it.
- Add one comparison to something the reader already knows, when one fits: SQL, a spreadsheet, a fab. Use only one.
- Say what the file does, never what the language does. No tutorial on decorators.
- Use the present tense. No sprint or leg names, and no history of how the file got this way.
- End with a pointer to the field guide section, if there is one.

A class or function docstring says what the thing holds or returns, and the one fact a caller would get wrong.
```

Draft: Coding Prompt:
"Each module you add or reshape gets a docstring per ADR-NNN. Write it last, when the file is finished, and read it against the file once more before handoff."

At first I didn't like that this was *written* last, because I *read* it first, but
after thinking about it, that is the best time to *write* it.

one-big-map `fields.py` and `dossier.py` are the two worked examples. The kit item [h-c0acc2] is where this is filed.