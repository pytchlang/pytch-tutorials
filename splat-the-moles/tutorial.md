# Splat the moles

We're going to write a game in Python where the player has to splat
moles to score points.  But if they miss, they lose all their points!
(Don't worry, no real moles will be harmed in making this game.)

---

TODO: Write tutorial

## Create a stage with backdrop

{{< commit add-Field-as-stage >}}


## Add the mole's holes

{{< commit add-Mole-with-all-empty >}}

{{< commit init-Mole-position-and-costume >}}


## Add actual mole costumes

{{< commit add-Mole-other-costumes >}}


## Pop out of random holes

{{< commit import-random >}}

{{< commit Mole-loop-random-holes >}}

{{< commit hide-Mole-between-popping-up >}}


## Set up scoring

{{< commit add-Mallet-set-up-scoring >}}

{{< commit show-score >}}


## Let player hit left hole

{{< commit add-Mallet-hit-left-basic >}}

{{< commit lose-points-if-miss-left >}}

{{< commit add-Mole-return-underground >}}

{{< commit Mallet-broadcast-left >}}


## Add sound effects

{{< commit add-Mallet-sounds >}}

{{< commit play-splat-if-hit-left >}}

{{< commit play-thud-if-miss-left >}}


## Let player hit other holes

{{< commit copy-paste-edit-for-centre >}}

{{< commit copy-paste-edit-for-right >}}


## Credits

We have used various freely-available resources to create this
project:

{{< asset-credits >}}
