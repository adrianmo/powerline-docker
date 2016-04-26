# vim:fileencoding=utf-8:noet
from powerline.segments import Segment, with_docstring
from powerline.theme import requires_segment_info
from requests.exceptions import ConnectionError
from docker import Client

class DockerSegment(Segment):

    def get_container_statuses(self):
        running = self.cli.containers(quiet=True, filters={'status': 'running'})
        paused = self.cli.containers(quiet=True, filters={'status': 'paused'})
        exited = self.cli.containers(quiet=True, filters={'status': 'exited'})
        restarting = self.cli.containers(quiet=True, filters={'status': 'restarting'})
        return (len(running), len(paused), len(exited), len(restarting))

    def build_segments(self, running, paused, exited, restarting):
        segments = [
            {'contents': u'\U0001F433 ', 'highlight_groups': ['docker'], 'divider_highlight_group': 'docker:divider'}
        ]

        if running:
            segments.append({'contents': ' ● %d' % running, 'highlight_groups': ['docker_running', 'docker'], 'divider_highlight_group': 'docker:divider'})
        if paused:
            segments.append({'contents': ' ~ %d' % paused, 'highlight_groups': ['docker_paused', 'docker'], 'divider_highlight_group': 'docker:divider'})
        if exited:
            segments.append({'contents': ' ✖ %d' % exited, 'highlight_groups': ['docker_exited', 'docker'], 'divider_highlight_group': 'docker:divider'})
        if restarting:
            segments.append({'contents': ' ➥ %d' % restarting, 'highlight_groups': ['docker_restarting', 'docker'], 'divider_highlight_group': 'docker:divider'})

        return segments

    def __call__(self, pl, base_url='unix://var/run/docker.sock'):
        self.pl = pl

        pl.debug('Running powerline-docker')

        self.cli = Client(base_url=base_url)

        try:
            running, paused, exited, restarting = self.get_container_statuses()
        except ConnectionError:
            pl.error('Cannot connect to Docker server on \'%s\'' % (base_url,))
            return
        except Exception as e:
            pl.error(e)
            return

        return self.build_segments(running, paused, exited, restarting)


docker = with_docstring(DockerSegment(),
'''Return the status of Docker containers.

It will show the number of Docker containers running and exited.
It requires Docker and docker-py to be installed.

Divider highlight group used: ``docker:divider``.

Highlight groups used: ``docker_running``, ``docker_exited``, ``docker``.
''')
