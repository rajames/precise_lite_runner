from math import floor


class Vectorizer:
    mels = 1
    mfccs = 2
    speechpy_mfccs = 3


class ListenerParams:
    window_t = 1.0
    hop_t = 0.02
    buffer_t = 1.96
    sample_rate = 16000
    sample_depth = 2
    n_mfcc = 13
    n_filt = 32
    n_fft = 256
    use_delta = False
    vectorizer = Vectorizer.mfccs
    threshold_config = ((6, 4),)
    threshold_center = 0.2

    @property
    def buffer_samples(self):
        samples = int(self.sample_rate * self.buffer_t + 0.5)
        return self.hop_samples * (samples // self.hop_samples)

    @property
    def n_features(self):
        print('buffer_samples', self.buffer_samples)
        print('window_samples', self.window_samples)
        print('self.hop_samples', self.hop_samples)
        return 1 + int(floor((self.buffer_samples
- self.window_samples) / self.hop_samples))

    @property
    def window_samples(self):
        return int(self.sample_rate * self.window_t + 0.5)

    @property
    def hop_samples(self):
        return int(self.sample_rate * self.hop_t + 0.5)

    @property
    def max_samples(self):
        return int(self.buffer_t * self.sample_rate)

    @property
    def feature_size(self):
        num_features = {
            Vectorizer.mfccs: self.n_mfcc,
            Vectorizer.mels: self.n_filt,
            Vectorizer.speechpy_mfccs: self.n_mfcc
        }[self.vectorizer]
        if self.use_delta:
            num_features *= 2
        return num_features


# Global listener parameters
params = ListenerParams()

