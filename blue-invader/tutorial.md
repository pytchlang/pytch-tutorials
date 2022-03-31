# Blue Invaders

In this game we'll defend ourselves from the dangerous blue invaders.
But don't destroy the friendly green aliens by mistake!


### Detailed credits

{{< asset-credits >}}


---

## Set the backdrop

{{< commit create-stage-with-backdrop >}}

## Create alien

{{< commit create-alien-with-costumes >}}

{{< commit loop-drift-down-screen >}}

{{< commit import-random >}}

{{< commit random-costume-per-descent >}}

## Make lots of aliens

{{< commit unrolled-make-clones >}}

{{< commit broadcast-make-clones >}}

{{< commit descend-on-play-game-broadcast >}}

{{< commit broadcast-play-game >}}

{{< commit define-glide-time >}}

{{< commit use-glide-time >}}

## Add sound effects

{{< commit add-alien-sounds >}}

{{< commit start-appropriate-sound-when-hit >}}

{{< commit hide-when-hit >}}

{{< commit show-when-starting-descent >}}

{{< commit add-sound-to-stage >}}

{{< commit make-miss-sound-when-stage-clicked >}}

## Keep score

{{< commit define-global-score >}}

{{< commit show-score >}}

{{< commit award-score-when-hit-enemy >}}

## Avoid repetitive code

{{< commit explicit-clone-start-locations >}}

{{< commit explicit-0-and-1-clone-start-locations >}}

{{< commit replace-repetition-with-loop >}}

## Count lives

{{< commit extract-lose-life-method >}}

{{< commit call-lose-life-method >}}

{{< commit define-global-lives >}}

{{< commit show-lives >}}

{{< commit decrement-lives >}}

## End game when no lives left

{{< commit define-global-game-over >}}

{{< commit set-game-over-when-no-lives >}}

{{< commit stop-descent-loop-when-game-over >}}

{{< commit broadcast-game-over >}}

{{< commit hide-when-receive-game-over >}}
