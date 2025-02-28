from playwright.sync_api import ViewportSize

class PlaywrightConfig:
    timeout = 30000  # 30 seconds
    base_url = 'http://localhost:3000'
    viewport = ViewportSize(width=1280, height=720)
    headless = False  # Set to True for CI/CD pipelines
    slow_mo = 100  # Slow down Playwright operations by 100ms
    
    @staticmethod
    def args():
        return {
            "timeout": PlaywrightConfig.timeout,
            "base_url": PlaywrightConfig.base_url,
            "viewport": PlaywrightConfig.viewport,
            "headless": PlaywrightConfig.headless,
            "slow_mo": PlaywrightConfig.slow_mo,
        }
