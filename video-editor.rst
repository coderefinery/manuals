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

The steps you should take:

1. Decide the total amount of time you will spend.  Probably no more
   than 2hr per half-day of teaching.
2. Open the .srt file. (it's a text file, but using a subtitle editor
   is probably worth it)

   - It is usually in the `video-processing repository
     <https://github.com/coderefinery/video-processing>`__.
   - You don't need to make it look perfect.  It should look useful.
     Grammar/spelling doesn't matter that much.  The times when
     Whisper stops including punctuation don't matter so much.
   - I usually correct unix commands (search `dash`, `hyphen`,
     `minus`, `dollar`, `space`) for example.  A learner is likely to
     try to read or copy these from the subtitles, even if they are in
     the video itself.
   - All names should be replaced with `[name]` (including instructor
     names).  This is probably done before you got the .srt file, but
     you can check.
   - Push it to git.

3. Create the editlist in the .yaml file.

   - The .yaml file should be pre-created and is usually in the course
     website repository or video-processing repository.
   - Make sure the session is there and has proper descriptions
   - Set the overall cut points for each session, break, and exercise
     (these are relatively easy to find)
   - Set timestamps for each new episode/section
   - Set timestamps for other important things learners may want to
     quickly find (important configuration, introducing exercises,
     etc.)

4. If you want, you can try generating the final videos yourself.  But
   the video uploader is likely to do this themselves anyway.  Some
   commands below:

   First, arrange files: compared to ``$PWD``, raw files are in
   ``raw/*{.mkv,.srt}``, and output gets written to ``out/``.  The
   .yaml editlist file can be in ``$PWD`` or somewhere else.

   First, run in check mode (``-c``) and limit to outputs matching
   day1 (``-l``). This will report any major errors.  If this passes,
   it's good enough For me to take over.  Look at .info.txt files to
   see if the description looks OK.

   .. code-block:: console

      $ ffmpeg-editlist ~/git/2025-03-25-workshop/video-editlist.yaml $PWD -c -l day1 --srt

   You can run and generate .mkv files, but don't re-encode (first few
   seconds are messed up).  You can see if .mkv looks roughly correct:

   .. code-block:: console

      $ ffmpeg-editlist ~/git/2025-03-25-workshop/video-editlist.yaml $PWD -l day1 --srt

   When it's all done, run with ``--reencode`` to create final files
   (you don't need to upload, video producer will regen):

   .. code-block:: console

      $ ffmpeg-editlist ~/git/2025-03-25-workshop/video-editlist.yaml $PWD -l day5 --srt --reencode


4. Push the .yaml to git and push the new .srt file via git.

   - Tell the main video manager it's done and they will check,
     encode, and upload to the respective places.



If the learner Zoom is recorded
-------------------------------

If learners may be in the recordings, they need detailed checking
before they can be posted.  See :doc:`video-checking` for the
preparation work and :doc:`video-editing` for the processing work.

In practice, if things are recorded this way, they are almost never
released because it is too much work and it never gets done.


Editing hints
-------------

- https://mpv.io is a command-line video player.
  - Hotkey ``O`` (capital letter O) to turn on time display
    permanently
  - Seek with left/right (~10 sec) or up/down (~ 1 minute)
  - - Run with ``--hr-seek`` to seek exactly, not to keyframes
  - https://github.com/Kr4is/mpv-copy-time - mpv script that lets you copy
    video times with a hotkey.  You might want to edit the hotkey by
    editing the script.
- How to run ffmpeg-editlist:
  - first with --check
  - then with no other
  - then --reencode
