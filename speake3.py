#! /usr/bin/env python3
from __future__ import print_function, with_statement
import os
import shlex
import subprocess
from queue import Queue
from multiprocessing.pool import ThreadPool


class GetOutput:
    # Class that executes espeak commands and returns output and/or err
    def __init__(self, cmd):
        self.__cmd = cmd
        args = shlex.split(self.__cmd)
        pipe = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.output = pipe.stdout.read().decode('utf-8')
        self.error = pipe.stderr.read().decode('utf-8')
        if self.output[-1:] == '\n':
            self.output = self.output[:-1]


class Speake:
    # Class that instantiates espeak-tts-engine objects.
    def __init__(self):
        self.espeak = 'espeak'
        self.a = ' -a '
        self.g = ' -g '
        self.p = ' -p '
        self.s = ' -s '
        self.f = ' -f '
        self.stdin = ' --stdin '
        self.k = ' -k '
        self.b = ' -b '
        self.l = ' -l '
        self.m = ' -m '
        self.q = ' -q '
        self.punct = ' --punct='
        self.split = ' --split='
        self.x = ' -x '
        self.v = ' -v '
        self.w = ' -w '
        self.z = ' -z '
        self.stdout = ' --stdout '
        self.version = ' --version '
        self.voices = ' --voices='
        self.command = ''
        self.commands = ''
        self.words = ''
        self.no = 0
        self.options = ()
        self.qu = Queue()
        self.output = object()
        self.status = object()
        self.status_output = ''
        self.status_error = ''
        # Condition to check if espeak-tts-engine is installed
        if not os.path.exists('/usr/bin/espeak'):
            raise OSError("Espeak text-to-speech engine is not installed in this system!")

    def __listoutput(self, voices):
        # Private function that converts output of get("voices") to a list of dictionaries
        keys = shlex.split(voices.splitlines()[0])
        voices_list = []
        for voice in voices.splitlines()[1:len(voices)]:
            voice_list = shlex.split(voice)
            voices_list.append(
                {keys[1]: voice_list[1], keys[2]: voice_list[2], keys[3]: voice_list[3],
                 keys[4]: voice_list[4]})
        return voices_list

    def set(self, option="", value=""):
        # Function that sets options or option+value pairs of the Speake instance
        self.options = (
            "textfile", "stdin", "amplitude", "wordgap", "capitals", "line-length", "pitch", "speed", "voice",
            "wavfile",
            "stdout", "version", "voices", "text-encoding", "markup", "quiet", "punct", "split", "write-pm", "nopause")
        if option in self.options:
            if self.options[0] == option:
                self.unset(option)
                self.f = self.f + "'" + value + "'"
                self.commands += self.f
            elif self.options[1] == option:
                self.unset(option)
                self.stdin += value
                self.commands += self.stdin
            elif self.options[2] == option:
                self.unset(option)
                self.a += value
                self.commands += self.a
            elif self.options[3] == option:
                self.unset(option)
                self.g += value
                self.commands += self.g
            elif self.options[4] == option:
                self.unset(option)
                self.k += value
                self.commands += self.k
            elif self.options[5] == option:
                self.unset(option)
                self.l += value
                self.commands += self.l
            elif self.options[6] == option:
                self.unset(option)
                self.p += value
                self.commands += self.p
            elif self.options[7] == option:
                self.unset(option)
                self.s += value
                self.commands += self.s
            elif self.options[8] == option:
                self.unset(option)
                self.v += value
                self.commands += self.v
            elif self.options[9] == option:
                self.unset(option)
                self.w = self.w + "'" + value + "'"
                self.commands += self.w
            elif self.options[10] == option:
                self.unset(option)
                self.stdout += value
                self.commands += self.stdout
            elif self.options[13] == option:
                self.unset(option)
                self.b += value
                self.commands += self.b
            elif self.options[14] == option:
                self.unset(option)
                self.m += value
                self.commands += self.m
            elif self.options[15] == option:
                self.unset(option)
                self.q += value
                self.commands += self.q
            elif self.options[16] == option:
                self.unset(option)
                self.punct += value
                self.commands += self.punct
            elif self.options[17] == option:
                self.unset(option)
                self.split += value
                self.commands += self.split
            elif self.options[18] == option:
                self.unset(option)
                self.x += value
                self.commands += self.x
            elif self.options[19] == option:
                self.unset(option)
                self.z += value
                self.commands += self.z
            else:
                return None
        else:
            return None

    def unset(self, option):
        # Function that unsets options of Speake instance
        if option in self.options:
            if self.options[0] == option:
                self.commands = self.commands.replace(self.f, "")
                self.f = self.f.replace(self.f, ' -f ')
            elif self.options[1] == option:
                self.commands = self.commands.replace(self.stdin, "")
                self.stdin = self.stdin.replace(self.stdin, ' --stdin ')
            elif self.options[2] == option:
                self.commands = self.commands.replace(self.a, "")
                self.a = self.a.replace(self.a, ' -a ')
            elif self.options[3] == option:
                self.commands = self.commands.replace(self.g, "")
                self.g = self.g.replace(self.g, ' -g ')
            elif self.options[4] == option:
                self.commands = self.commands.replace(self.k, "")
                self.k = self.k.replace(self.k, ' -k ')
            elif self.options[5] == option:
                self.commands = self.commands.replace(self.l, "")
                self.l = self.l.replace(self.l, ' -l ')
            elif self.options[6] == option:
                self.commands = self.commands.replace(self.p, "")
                self.p = self.p.replace(self.p, ' -p ')
            elif self.options[7] == option:
                self.commands = self.commands.replace(self.s, "")
                self.s = self.s.replace(self.s, ' -s ')
            elif self.options[8] == option:
                self.commands = self.commands.replace(self.v, "")
                self.v = self.v.replace(self.v, ' -v ')
            elif self.options[9] == option:
                self.commands = self.commands.replace(self.w, "")
                self.w = self.w.replace(self.w, ' -w')
            elif self.options[10] == option:
                self.commands = self.commands.replace(self.stdout, "")
                self.stdout = self.stdout.replace(self.stdout, ' --stdout ')
            elif self.options[13] == option:
                self.commands = self.commands.replace(self.b, "")
                self.b = self.b.replace(self.b, ' -b ')
            elif self.options[14] == option:
                self.commands = self.commands.replace(self.m, "")
                self.m = self.m.replace(self.m, ' -m ')
            elif self.options[15] == option:
                self.commands = self.commands.replace(self.q, "")
                self.q = self.q.replace(self.q, ' -q ')
            elif self.options[16] == option:
                self.commands = self.commands.replace(self.punct, "")
                self.punct = self.punct.replace(self.punct, ' --punct=')
            elif self.options[17] == option:
                self.commands = self.commands.replace(self.split, "")
                self.split = self.split.replace(self.split, ' --split=')
            elif self.options[18] == option:
                self.commands = self.commands.replace(self.x, "")
                self.x = self.x.replace(self.x, ' -x ')
            elif self.options[19] == option:
                self.commands = self.commands.replace(self.z, "")
                self.z = self.z.replace(self.z, ' -z ')
        else:
            return None

    def get(self, option, value=""):
        # Function that gets read only properties of the Speake instance
        if option in ("version", "voices"):
            if option is "version":
                self.output = GetOutput(self.espeak + self.version)
                return self.__listoutput(self.output.output)
            elif option is "voices":
                self.output = GetOutput(self.espeak + self.voices + value)
                return self.__listoutput(self.output.output)
        else:
            return None

    def say(self, words=""):
        # Function where words to be said are passed to Speake object and added to the command Queue
        self.words = words
        self.command = self.espeak + self.commands + ' "' + self.words + '"'
        self.qu.put(self.command)
        self.no += 1

    def talkback(self):
        # Function that creates threads depending on the number of calls to say().Each thread makes a call to Getoutput
        # class where actual execution occurs
        if self.words == "":
            self.say()
            pool = ThreadPool(1)
            for n in range(self.no):
                if self.qu.empty():
                    break
                else:
                    self.status = pool.apply(GetOutput, (self.qu.get(),))
                    self.status_output += self.status.output
                    self.status_error += self.status.error
        else:
            pool = ThreadPool(1)
            for n in range(self.no):
                if self.qu.empty():
                    break
                else:
                    self.status = pool.apply(GetOutput, (self.qu.get(),))
                    self.status_output += self.status.output
                    self.status_error += self.status.error
