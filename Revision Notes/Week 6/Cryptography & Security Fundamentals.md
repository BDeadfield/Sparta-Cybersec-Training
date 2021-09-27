# Cryptography

**Cryptography** or cryptology is the study of secure communication techniques used by a sender in order to ensure only the desired recipents can view the message. It Can be used to protect confidential data, as well as Helping to ensure the integrity of data.

**Cryptanalysis** is the study and practice of exploiting and breaking cryptographic techniques.

**Encryption** is the process of scrambling plain-text into "ciphertext", and **decryption** is the reverse. This process is closely associated with cryptography for it's use in secure communnicaiton.

## Ciphers

A **cipher** is an algorithm which is used for encryption or decryption (i.e Substitution, Caesar, Transposition).

**Block** ciphers transform a fixed-length "block" of plain-text into a block ciphertext (64 or 128 bits). **Stream** ciphers encrypt plain-text one bit or byte at a time and are typically faster.

## Symmetric Ciphers

Symmetric Ciphers are the simplest method of encryption, which utilizes a secret key in order to encrypt data. This data is sent along with the secret key, which can be used to decrypt.

- **DES** is a legacy encryption algorithm that can be used in both block and stream mode
- **3DES** is a modern version of DES, which follows the same process, but three times over. This takes longer to compute, however it features better security.
- **AES** is more secure than 3DES, and because of this it is a popular recommended algorithm. It offers nine combinations of key and block length.
- **SEAL** is a fast alternative algorithm to DES, 3DES and AES. It is a stream cipher that utilizes a 160-bit encryption key.
- **RC** including RC2, RC4, RC5 and RC6 (RC4 being the most prevalent). RC4 is a stream cipher, which is often used to secure web traffic in SSL and TLS.

## Asymmetric Ciphers

Asymmetric ciphers also know as public key algorithms, is where each user has a public / private key, a sender will request the recipents public key, before using it to encrypt the message prior to sending it. When the recipent recieves the message, they will use their private key to decrypt the message.

- **Diffie-Hellman** is a way of exchanging cryptographic keys. Diffie-Hellman utilizes a pre-shared key, which is added to each user's private key to create a sum, which will be exchanged with the other user, the other user will then proceed to add their private key to the other user's sum, which will result in an identical key on both sides.
- **ElGamal** is based on the diffie hellman method, however encrypted messages become much larger, and because of this is only used for small amounts of data, such as secret keys.
- **RSA** is an algorithm based on factoring large numbers due to it's current difficulty. It is the first algorithm considered suitable for signing as well as encryption.
- **Digital Signature Standard** or DSS specifies **DSA** as it's algorithm for digital signatures, which is based on the ElGamal signature scheme. Creation speed is similar to RSA but is much slower for verification.
- **Eliptical Curve** techniques can be used in order to adapt other cryptographic algorithms, such as Diffie-Hellman or ElGamal. The main advantage of Eliptical Curve techniques are their much smaller key sizes.

## Principles

Secure communication consists of four elements:
- **Confidentiality** guarantees that only the authorized users can read the message. The message cannot be decrypted in a reasonable amount of time.
- **Integrity** guarantees that the message has not be altered in transit utilizing hash-generating techniques, such as Message Digest v5 (MD5) or Secure Hash Algorithm (SHA). This is guaranteed by only one user having access to a key.
- **Origin Authentication** guarantees that the message has come from the expected sender and is not a forgery. This is guaranteed by only one user having access to a key.
- **Data Non-Repudiation** guarantees that a user can be held accountable for their actions based on logs and comparing keys utilized.

## Hashing

**Hashing** is a one-way mathematical operation, which generates a message digest (fixed-length hexadecimal string). This message digest can be utilized for ensuring data integrity, as well as authentication. The message digest is relatively easy to produce, but much harder to reverse.

**MD5** uses a 128-bit digest and is considered legacy. **SHA1** uses a 160-bit digest and is also considered legacy. **SHA2** includes SHA-224, SHA-256, SHA-384 and SHA-512 and is the modern-generation of algorithms.

**Brute Force** is a way hashes can be broken by repeatedly hashing strings in an attempt to match a desired hash. **Rainbow Table** attacks are similar to brute force attacks, however they will utilize a table of pre-defined hashes for comparison. **Dictionary** attacks differ from brute force attacks based on their scope, as dictionary attacks focus on common / popular words or passwords.

**Salting** is the procedure of adding generated data at the end of a mesaage before hashing it, in order to increase it's complexitiy to make it harder to be exploited.

**HMAC** or Hash Message Authentication Code, is the process of hashing a message alongside a secret key (which only the sender and receiver will have), this secret key will be necessary in order to calculate the message digest of the HMAC. This ensures authenticity in the origin of the message.

## Public Key Infrastructure

Public Key Infrastructure (PKI) is an example of a trusted-third party system also known as certificate authority (CA). The CA will provide authentication to users in the form of a digital certicate, which users will recognize as being validated by the CA. This allows for large-scale distribution and scalability of trust relationships using public keys.

**Single-root** topologies utilizes a singluar CA in order to issue certificates to end-users, which are usually in the same organisation.
**Cross-certified** topologies utilize a peer-to-peer model to establish trust with other CAs in order to provide trust amongst their domains.
**Hierarchical** topologies utilize root CA's to issue certificates to subordinte CA's, which further issue certificates to end-points.

**Digital Signatures** are a mathematical technique which produce a signature that cannot be forged, reused in another document and prevent the alteration of a document after signing. **DSA, RSA and Eliptic Curve Digital Signature** algorithms can be used in order to produce digital signatures. They are used to provide:
- Authenticity by proving an individual has seen and signed the data
- Integrity by proving the data hasn't been modified since signing
- Non-repudiation by proving that the transaction of data did in fact take place.

**Code signing** is a way digital signatures are used in order to provide integrity for executable files downloaded from a website as well as authentication to verify the identity of the website.

**Digital Certificates** are another way digital signatures are used in a manner similar to an ID card in order to verify a website and establish an encrypted connection. These will include details on:
- Public key
- Usage
- CA Issuer
- Valid Date Range
- Algorithm Used to Create Signature

**Secure Socket Layer** or SSL, is an encryption-based security protocol that is utilized in order to ensure confidentiality, authenticaion and integrity of data in Internet communications, known as HTTPs communications. SSL is the predecessor of TLS. SSL and TLS utilize digital certificates in order to encrypy communicaitons.

**Secure Shell** or SSH, is a network communication protocol used for encrypted communication to a computer / server requiring a login, and is a more secure alternative to telnet or FTP.

## Misc.

**Base64** is a form of encoding (does not require a secret key to decrypt, only encode type) that can be used in order to ensure data remains intact during transport.

# Cybersecurity Fundamentals

## Authentication, Authorization and Accounting (AAA)

The AAA framework is a simple way to understand security issues surrounding users access of resources and / or systems. The AAA framework utilizes the priniciple of authenticaton to attain the identify of the user, authorization to manage the user's access of resources and accounting to maintain a detailed log of actions taken to hold user's accountable.

**AAA Server** can be utilized in order to handle user requests for access to systems or resources.

## Access Control Methods

- **Discretionary** based is the least restrictive and provides the creator or anyone with permissions to the resource the utility to allocate user permissions.
- **Role** based provides access to resources based on position or role within a company / organisation.
- **Rule** based provides dynamic access to a resource based on criteria defined by an administrator (i.e role, location, time)
- **Attribute** based provides access based on certain details associated with a user, such as location, user type or department.
- **Time** based provides users access based on an alloted time period.
- **Least Priviledge** based provides access to only those who require it and no one else.
