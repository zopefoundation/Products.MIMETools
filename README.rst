.. image:: https://github.com/zopefoundation/Products.MIMETools/actions/workflows/tests.yml/badge.svg
        :target: https://github.com/zopefoundation/Products.MIMETools/actions/workflows/tests.yml

.. image:: https://coveralls.io/repos/github/zopefoundation/Products.MIMETools/badge.svg
        :target: https://coveralls.io/github/zopefoundation/Products.MIMETools

.. image:: https://img.shields.io/pypi/v/Products.MIMETools.svg
        :target: https://pypi.org/project/Products.MIMETools/
        :alt: Current version on PyPI

.. image:: https://img.shields.io/pypi/pyversions/Products.MIMETools.svg
        :target: https://pypi.org/project/Products.MIMETools/
        :alt: Supported Python versions

Products.MIMETools
==================

Currently, the MIMETools product's only function is to provide the
``<dtml-mime>`` DTML tag for the DocumentTemplate distribution.

The ``<dtml-mime>`` tag is used to construct MIME containers. The syntax of the
``<dtml-mime>`` tag is::

  <dtml-mime type="x" disposition="y" encode="z">
  Contents of first part
  <dtml-boundary type="x" disposition="y" encode="z">
  Contents of second part
  <dtml-boundary type="x" disposition="y" encode="z">
  Contents of nth part
  </dtml-mime>

The area of data between tags, called a block, is encoded into whatever is
specified with the 'encode' tag attribute for that block. If no encoding is
specified, 'base64' is defaulted. Valid encoding options include 'base64',
'quoted-printable' and '7bit' . If the 'encode' attribute is set to '7bit'
no encoding is done on the block and the data is assumed to be in a valid MIME
format.

If the 'disposition' attribute is not specified for a certain block, then the
'Content-Disposition:' MIME header is not included in that block's MIME part.

The entire MIME container, from the opening mime tag to the closing, has it's
'Content-Type:' MIME header set to 'multipart/mixed'.

For example, the following DTML::

  <dtml-mime encode="7bit" type="text/plain">
  This is the first part.
  <dtml-boundary encode="base64" type="text/plain">
  This is the second.
  </dtml-mime>

Is rendered to the following text::

  Content-Type: multipart/mixed;
      boundary="216.164.72.30.501.1550.923070182.795.22531"

  --216.164.72.30.501.1550.923070182.795.22531
  Content-Type: text/plain
  Content-Transfer-Encoding: 7bit

  This is the first part.

  --216.164.72.30.501.1550.923070182.795.22531
  Content-Type: text/plain
  Content-Transfer-Encoding: base64

  VGhpcyBpcyB0aGUgc2Vjb25kLgo=

  --216.164.72.30.501.1550.923070182.795.22531--

The ``dtml-mime`` tag is particularly handy in conjunction with the
``dtml-sendmail`` tag.  This allows Zope to send attachments along with email.
Here is an example.

Create a DTML method called 'input' with the following code::

  <dtml-var standard_html_header>
  <form method="post" action="send" ENCTYPE="multipart/form-data">
  <input type="file" name="afile"><br>
  Send to:<input type="textbox" name="who"/><br/>
  <input type="submit" value="Send"/>
  </form>
  <dtml-var standard_html_footer>

Create another DTML Method called 'send' with the following code::

  <dtml-var standard_html_header>
  <dtml-sendmail smtphost="localhost">
  From: michel@digicool.com
  To: <dtml-var who>
  <dtml-mime type="text/plain" encode="7bit">

  Hi <dtml-var who>, someone sent you this attachment.

  <dtml-boundary type="application/octet-stream" disposition="attachment"
  encode="base64"><dtml-var "afile.read()"></dtml-mime>

  </dtml-sendmail>

  Mail with attachment was sent.
  <dtml-var standard_html_footer>


Notice that there is no blank line between the 'To:' header and the starting
``dtml-mime`` tag. If a blank line is inserted between them then the message
will not be interpreted as multipart by the receiving mail reader.

Also notice that there is no newline between the ``dtml-boundary`` tag and the
``dtml-var`` tag, or the end of the ``dtml-var`` tag and the closing
``dtml-mime`` tag. This is important, if you break the tags up with newlines
then they will be encoded and included in the MIME part, which is probably not
what you want.

As per the MIME spec, ``dtml-mime`` tags may be nested within ``dtml-mime``
tags arbitrarily.
