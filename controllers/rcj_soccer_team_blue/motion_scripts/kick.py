
kick = MotionScript(
    name="kick",
    stages=[
        Stage(
            target=[
                Target(move=-5)
            ],
            time = 1
        ),
        Stage(
            target=[
                Target(move=5)
            ],
            time = 0.5
        )

]
)
