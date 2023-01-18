import numpy as np

class BackgroundSource:
    def __init__(self, r_b : float, mu_Eb : float, sigma_Eb: float):
        self.r_b = r_b
        self.mu_Eb = mu_Eb
        self.sigma_Eb = sigma_Eb
        pass
    # MORE CODE HERE, IF NECESSARY

class Detector:
    def __init__(self, R : float, delta_Erec: float, background_source : BackgroundSource):
        self.R = R
        self.delta_Erec = delta_Erec
        self.background_source = background_source
        pass

    def generate_background(self, T : int):
        # Generate the number of background events
        num_events = int(self.background_source.r_b * T)
        
        # Generate random x, y, z coordinates within the sphere
        x = (np.random.rand(num_events) - 0.5) * 2 * self.R
        y = (np.random.rand(num_events) - 0.5) * 2 * self.R
        z = (np.random.rand(num_events) - 0.5) * 2 * self.R
        
        # Generate random direction cosines
        d_x = np.random.rand(num_events) - 0.5
        d_y = np.random.rand(num_events) - 0.5
        d_z = np.random.rand(num_events) - 0.5
        
        # Generate random times between 0 and T
        t = np.random.rand(num_events) * T
        
        # Generate true energies with normal distribution
        E_true = np.random.normal(self.background_source.mu_Eb, self.background_source.sigma_Eb, num_events)
        
        # Generate reconstructed energies with normal distribution
        E_rec = np.random.normal(E_true, self.delta_Erec * E_true, num_events)
        
        # Create an array of the events
        events = np.column_stack((x, y, z, d_x, d_y, d_z, t, E_true, E_rec))
        
        return events

    # MORE CODE HERE, IF NECESSARY