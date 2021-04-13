# conlang

<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [conlang](#conlang)
- [Introduction](#introduction)
- [Features](#features)
- [Formats](#formats)
	- [Graphical](#graphical)
	- [Typed](#typed)
- [Ambiguity](#ambiguity)
- [Syntax](#syntax)
- [Examples](#examples)
	- [English](#english)
	- [Parsing](#parsing)
- [Translation](#translation)
	- [To Other Languages](#to-other-languages)
	- [From Other Languages](#from-other-languages)
- [Speech](#speech)
	- [Pronunciation](#pronunciation)
	- [Text to Speech](#text-to-speech)
	- [Speech to Text](#speech-to-text)
- [Variations](#variations)
	- [Artistic](#artistic)

<!-- /TOC -->

# Introduction

S'von! This repository stores data and scripts associated with my (as of yet unnamed) personal conlang (short for [constructed language](https://en.wikipedia.org/wiki/Constructed_language)). This project serves a few purposes;

 - Speeding up both digital and traditional note-taking
   - Hypothesis that translating notes while writing them could also aid comprehension and retention
 - Better understanding language systems and dynamics as I dive deeper into Natural Language Processing (NLP)
 - Providing an efficient and precise interface for personal NLP-based systems (primarily a digital assistant I have been working on)

Anyone is free to use these tools if they find them helpful, although it should be noted that minimal attention was paid to making them universally helpful/easy to learn.

# Features

The following is a non-exhaustive list of guiding principles and features the language is intended to have.

 - **Efficiency**
 - **Standardization**
 - **Flexibility**
 - **Coverage**
 - **Modularity**
 - **Integration**
 - **Simplicity**
 - **Longevity**

# Formats

The language can be written in two main forms; graphically and typed. The latter is a Romanized version that can be written using universal ASCII/Unicode characters; it is useful for interacting with NLP systems, communicating via text, etc.

## Graphical

This is usually the most efficient way to write in the language by hand, and is based upon a flexible hierarchy of symbols. It is limited in portability, so the typed version may be preferred for communication or when using certain mediums.

## Typed

The alphabet includes the same letters as the 26-character English alphabet, although the pronunciations of many letters and syllables deviate from their English counterparts.   

# Ambiguity

This particular conlang is designed to be completely semantically unambiguous when possible, mainly to facilitate computer parsing and generation of statements. Therefore, only one meaning can be extracted from a statement and it can be processed with no loss of precision. This is achieved by specifically designating modifiers to subjects and objects so that no subjectivity is involved in interpretation.

# Syntax

# Examples

## English

Some examples of simple statements (original meanings in English)

 - `I will become a very powerful king.` **&#8594;** ``Zev jet'ulad wesane`x'ret'ama.``

## Parsing

Examples for how meaning can be algorithmically extracted from statements.

*Note: this section covers automated parsing of text-based statements; parsing is not necessary for a natural tree as it represents the semantic meaning of the statement.*

``Zev jet'ulad wesane`x'ret'ama.``

1. Identify sentence bounds from capitalization and punctuation (very similar to other languages)
2. Locate subject, verb, and object; `Zev`; `jet'ulad`; ``wesane`x'ret'ama``
3. Parse each of the above into roots and modifiers
      - `zev`
      - `je`; `ulad`
      - `wesane`; `ret`; `ama`
4. Group modifiers
      - `ret` + `ama`
5. Generate parse tree
  - Subject: `zev`
  - Verb: `ulad`
    - Tense: `je`
  - Object: `wesane`
    - Modifier: `ret`
      - Modifier: `ama`

# Translation

## To Other Languages

## From Other Languages

# Speech

## Pronunciation

## Text to Speech

## Speech to Text

# Variations

## Artistic

A branch of this language is planned to accommodate more nuanced and aesthetically-pleasing words and phrases. The syntax will remain mostly the same.
