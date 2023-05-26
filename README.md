[amplitude]: https://github.com/aspiringLich/amplitude
[TOML]: https://toml.io/en/

# Amplitude Articles

This repository stores the articles for [amplitude].

We welcome contributions to this repository. Before you commit however, here's some details on how stuff is laid out.

> ### **PLEASE NOTE:** This stuff can and WILL change.

Every top level directory represents a **course**. Each course contains **tracks** which are a collection of **items**. For more detail on items see the [Items](#items) section.

## Directory Structure

```
amplitude_articles/
├ my_course/
│ ├ my_track1/
│ │ ├ +track.toml
│ │ └ ...
│ ├ my_track2/
│ │ ├ +items.toml
│ │ └ ...
│ ├ config.toml
│ ├ header.md
│ └ index.md
...
```

### `config.toml`

This file contains metadata about the course.

```toml
# The name of the course
name = "Testing Course"
description = "I'm using this to test stuff out"

tracks = [
    "my-track1",
    "my-track2",
]
```

### `header.md`

This file contains the header for the course. Basically you put markdown links that you want to be able to use in any of your articles. It does not have a config header.

### `index.md`

This file contains the markup for the course's index page. It does not have a config header.

### `+track.toml`

This file contains information about the track. It defines general information as well as a list of items. It is very similar to the `config.toml` file.

```toml
name = "My Track One"
description = "This is track number one!"
```

## Items

### Article

An article has a config header that defines metadata about the article. Writing the main heading of an article is not necessary, it will be automatically inserted in.

```toml
---
title = "My Article"
---

## Subheading

bla bla bla bla bla bla...
```

### Quiz

Quizzes are defined with a toml file. Should be pretty self explanatory.

````toml
[[questions]]
answers = [
    {text = "~~~txt\nHello World!\nYou said: a", response = "yay", correct = true},
    {text = "~~~txt\nHello World!\nYou said: b", response = "no"},
    {text = "~~~txt\na", response = "I mean, close?"},
    {text = "~~~txt\nisadoai\ndaskfaifj\n~~~", response = "what?"},
]
question = """
Consider the following code:

@code rust

    use std::io;

    fn main() {
        println!("Hello, world!");
        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();
        println!("You said: {input}");
    }

If i run this code, and type `a`, what will be printed?
"""
````

### Exercise

Exercises are defined with a file of the language of choice.

 
