---
title:  'Great Talk'
author: Prof. Dr. Me Ofcourse
shortauthor: M Ofcourse
date: 17.2.2016
institute: Institute for Psychology, University of Tromsø, Norway
instituteshorthand: UiT - Tromsø
toc: true
logo: pics/uit.png
logowidth: .8\textwidth
header-includes:
  - \renewenvironment{quote}{\begin{center}}{\end{center}}
output:
  beamer_presentation:
    toc: true
    keep_tex: true
    slide_level: 1
    theme: "templates/amsterdam.beamer"
    highlight: tango  
...

# Notes

- the stuff after `output` in the preamble is so that the `atom`-package [markdown-preview-enhanced](https://github.com/shd101wyy/markdown-preview-enhanced) also works properly
- all the rest is specified in the latex-templates and the `Makefile`

# Slide 1

- Bullett point

. . .

- pause on slide

# Centering stuff

> I redefined the `>` symbol to result in a center-environment
> can be used with images, too

> ![](pics/stan.png){ width=30% }

# citations

work [@open2015estimating] in case you use pandoc-citeproc


# Pictures

![Stan's logo with a caption and figure number, custom width.](pics/stan.png){ width=60% }

# Pictures without captions

Use a backslash after the picture

![](pics/stan.png){ width=30% } \


So that you don't get a caption. (two empty lines after)

# Paused bullet points

> 1. number one
> 2. and two

> - works with normal ones
> - as well
-

---

slide without title


# Latex slide

\begin{minipage}{\textwidth}
\begin{minipage}{.5\textwidth}
  \includegraphics[width=\textwidth]{pics/stan.png}
\end{minipage}
\hfill
\begin{minipage}{.45\textwidth}
  \begin{itemize}
  \item markdown
  \item does
  \item not work here
  \end{itemize}
\end{minipage}
\end{minipage}

# multi-column slide in markdown

\begincols{}

\column{0.3\textwidth}

![](pics/stan.png)\

\column{0.7\textwidth}


found this in <https://github.com/jgm/pandoc/issues/1710>

- this
- **has**
    - full [markdown]() support!


\stopcols

# multi-columns using the new markdown-syntax


:::::::::::::: {.columns}
::: {.column width="35%"}
## block 1
contents...
:::
::: {.column width="60%"}
## block 2
contents...
:::
::::::::::::::



# A full slide can be shrunk {.shrink}

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam risus sem, consectetur ac dui non, mattis egestas sem. Quisque sit amet mi lacus. Mauris porta lacus sapien, ac tempor nisl faucibus ut. Aenean tristique nibh ut mauris pretium, eget pellentesque erat suscipit. Vivamus ornare ex fringilla dapibus blandit. Nam sodales tincidunt nisl at bibendum. In porta, dolor at rutrum varius, nulla nulla tincidunt diam, ut vestibulum turpis mi eu tellus. Curabitur id dolor placerat, efficitur sapien eget, fermentum diam. Mauris sodales mattis rutrum. Cras varius lobortis fringilla. Phasellus magna mauris, ornare nec maximus in, ultricies nec dui. Quisque laoreet ullamcorper metus, a scelerisque lacus sodales sed.

Cras rhoncus laoreet felis, id consequat nisi ullamcorper vel. Maecenas ut augue arcu. Fusce eu fringilla elit. Nullam consectetur porta odio id varius. Duis imperdiet libero vitae mauris semper, imperdiet lacinia est interdum. Interdum et malesuada fames ac ante ipsum primis in faucibus. Duis cursus felis quam, quis mollis lacus euismod non. Nullam tortor mauris, vehicula at molestie a, sagittis sed sapien. Nam finibus sodales felis. Integer tincidunt mollis convallis. Donec id eleifend odio.

Nunc quis convallis odio. Sed finibus id ipsum non molestie. Morbi dignissim scelerisque fermentum. Aenean volutpat eros sem. Suspendisse a ante luctus, vehicula nisl et, accumsan augue. Praesent luctus gravida luctus. Sed dictum imperdiet orci. Proin accumsan condimentum porttitor. Aliquam efficitur neque non venenatis elementum. Mauris ut diam a neque condimentum condimentum eget sit amet ante.

Nullam molestie ultrices enim at viverra. Donec tristique vel ante id tincidunt. Fusce bibendum nibh in ligula tincidunt, blandit molestie nulla eleifend. Phasellus pulvinar velit libero, a sollicitudin diam egestas non. Pellentesque eu turpis efficitur, blandit lectus et, venenatis nulla. Etiam quis auctor lorem. In nec lacinia lorem. Lorem ipsum dolor sit amet, consectetur adipiscing elit. In porttitor diam vitae ipsum molestie, a semper erat vulputate. Suspendisse sit amet scelerisque magna, ac porta ligula.


# References {.allowframebreaks}

Enable allowframebreaks so that the list can be spread out across many slides
