# vim:fileencoding=utf-8:noet
from powerline.segments import Segment, with_docstring
from powerline.theme import requires_segment_info
from docker import Client

@requires_segment_info
class DockerSegment(Segment):

    def get_container_statuses():
        running = cli.containers(quiet=True, filters={'status': 'running'})
        exited = cli.containers(quiet=True, filters={'status': 'exited'})
        return (len(running), len(exited))

    def build_segments(self, running, exited):
        segments = [
            {'contents': u'\ue0a0 ', 'highlight_groups': ['docker'], 'divider_highlight_group': 'docker:divider'}
        ]

        if running:
            segments.append({'contents': ' ● %d' % running, 'highlight_groups': ['docker_running', 'docker'], 'divider_highlight_group': 'docker:divider'})
        if exited:
            segments.append({'contents': ' ✖ %d' % exited, 'highlight_groups': ['docker_running', 'docker'], 'divider_highlight_group': 'docker:divider'})

        return segments

    def __call__(self, pl, segment_info):
        pl.debug('Running powerline-docker')

        self.cli = Client(base_url='unix://var/run/docker.sock')

        running, exited = self.get_container_statuses()

        return self.build_segments(running, exited)


docker = with_docstring(DockerSegment(),
'''Return the status of Docker containers.
''')
