import os
import sys
import logging
import delegator
from abc import ABCMeta, abstractmethod
from future.utils import with_metaclass
from tempfile import NamedTemporaryFile
from PyInquirer import style_from_dict, Token, prompt


logger = logging.getLogger(__name__)


class BaseCommitizen(with_metaclass(ABCMeta)):

    style = style_from_dict({
        Token.Separator: '#6C6C6C',
        Token.QuestionMark: '#FF9D00 bold',
        Token.Selected: '#5F819D',
        Token.Pointer: '#FF9D00 bold',
        Token.Instruction: '',  # default
        Token.Answer: '#5F819D bold',
        Token.Question: '',
    })

    @abstractmethod
    def questions(self):
        """Questions regarding the commit message.

        Must have 'whaaaaat' format.
        More info: https://github.com/finklabs/whaaaaat/

        :rtype: list
        """

    @abstractmethod
    def message(self, answers):
        """Format your git message.

        :param answers: Use answers
        :type answers: dict

        :rtype: string
        """

    @staticmethod
    def commit(message, add_all=True):
        f = NamedTemporaryFile('wb', delete=False)
        f.write(message.encode('utf-8'))
        f.close()
        cmd = "git commit "
        if add_all:
            cmd += "-a"
        c = delegator.run('{0} -F {1}'.format(cmd, f.name))
        print(c.out or c.err)

        os.unlink(f.name)
        return c

    def example(self):
        """Example of the commit message.

        :rtype: string
        """
        raise NotImplementedError("Not Implemented yet")

    def schema(self):
        """Schema definition of the commit message.

        :rtype: string
        """
        raise NotImplementedError("Not Implemented yet")

    def info(self):
        """Information about the standardized commit message.

        :rtype: string
        """
        raise NotImplementedError("Not Implemented yet")

    def show_example(self, *args, **kwargs):
        logger.info(self.example())

    def show_schema(self, *args, **kwargs):
        logger.info(self.schema())

    def show_info(self, *args, **kwargs):
        logger.info(self.info())

    def run(self, *args, **kwargs):
        questions = self.questions()
        answers = prompt(questions, style=self.style)
        logger.debug('Answers:\n %s', answers)
        m = self.message(answers)
        logger.debug('Commit message generated:\n %s', m)

        cl = args[0]  # command line args
        err = None
        out = None
        if cl.file is None:
            c = self.commit(m, cl.all)
            err = c.err
            out = c.out
        else:
            try:
                with open(cl.file, "w") as _f:
                    _f.write(m)
                    logger.info("File {} written".format(cl.file))
            except Exception as _e:
                err = str(_e)

        if err:
            logger.warning(err)
            sys.exit(1)

        if cl.file is None and 'nothing added' not in out:
            logger.info('Commit successful!')

        sys.exit(0)
