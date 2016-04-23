# vim:fileencoding=utf-8:noet
from powerline.segments import Segment, with_docstring
from powerline.theme import requires_segment_info

@requires_segment_info
class DockerSegment(Segment):
    pass

docker = with_docstring(DockerSegment(),
'''Return the status of Docker containers.
''')
