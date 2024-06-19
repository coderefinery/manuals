Video editor
============

The video editor takes the raw recorded files from the broadcaster,
processes them, and uploads them to YouTube (or whatever).



Overall priorities
------------------

1. No learner (or anyone not staff) video, audio, names, etc. are
   present in the recordings.

2. Good descriptions.

3. Removing breaks and other dead time.

4. Splitting videos into useful chunks (e.g. per-episode), perhaps
   equal with the next one:

5. Good Table of Contents information so learners can jump to the
   right spots (this also helps with "good description".)


Modern: livestream method
-------------------------

Modern livestream courses produce videos without any learners in
them.  In this case, using
https://github.com/coderefinery/ffmpeg-editlist is sufficient.  Look
at that repo for instructions.  As an example, check out
https://github.com/AaltoSciComp/video-editlists-asc for some past
workshops.  For example, ``kickstart-2022-winter.yaml`` is a
reasonable starting point to copy.

It's our standard to have these videos on YouTube by the same evening
the course is held.  It may be hard, but it's better to reduce the
quality to make it happen quickly than wait a while to get it perfect
(otherwise it might not happen at all).



If the learner Zoom is recorded
-------------------------------

If learners may be in the recordings, they need detailed checking
before they can be posted.  See :doc:`video-checking` for the
preparation work and :doc:`video-editing` for the processing work.

In practice, if things are recorded this way, they are almost never
released because it is too much work and it never gets done.
