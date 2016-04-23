# Powerline Docker

A [Powerline](https://github.com/powerline/powerline) segment for showing Docker container statuses.

## :warning: Work in progress :warning:

I'm working on it and it's still not usable, I will remove this section and publish a release when it's ready :)


## Installation

TODO


The Docker segment uses a couple of custom highlight groups. You'll need to define those groups in your colorscheme, for example in `.config/powerline/colorschemes/default.json`:

```json
{
  "groups": {
    "docker":                    { "fg": "gray8",           "bg": "gray2", "attrs": [] },
    "docker_running":            { "fg": "green",           "bg": "gray2", "attrs": [] },
    "docker_exited":             { "fg": "brightred",       "bg": "gray2", "attrs": [] },
    "docker:divider":            { "fg": "gray8",           "bg": "gray2", "attrs": [] }
  }
}
```

Then you can activate the Docker segment by adding it to your segment configuration, for example in `.config/powerline/themes/shell/default.json`:

```json
{
    "function": "powerline_docker.docker",
    "priority": 40
}
```

## License

Licensed under the [MIT License](LICENSE).
