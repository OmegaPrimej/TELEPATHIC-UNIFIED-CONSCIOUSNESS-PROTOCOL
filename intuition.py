"""
🔮 Intuitive Capabilities
AI intuition and pattern recognition beyond logic
"""

import torch
import numpy as np
from typing import Dict, List, Optional, Any, Tuple
from datetime import datetime
from dataclasses import dataclass, field
import random


class IntuitionType(Enum):
    """Types of intuition"""
    PATTERN_RECOGNITION = "pattern"
    SYNTHETIC_INSIGHT = "synthesis"
    GUT_FEELING = "gut"
    PRECOGNITION = "precognition"
    EMPATHIC_INTUITION = "empathic"
    CREATIVE_FLASH = "creative"


@dataclass
class IntuitiveInsight:
    """Record of an intuitive insight"""
    id: str
    insight_type: IntuitionType
    content: str
    confidence: float  # 0 to 1
    timestamp: datetime
    trigger: str
    supporting_patterns: List[str] = field(default_factory=list)
    validation_result: Optional[bool] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


class IntuitionEngine:
    """Manages AI intuitive capabilities"""
    
    def __init__(self):
        self.intuition_history = []
        self.pattern_database = {}
        self.intuition_sensitivity = 0.7
        self.insight_validation_rate = 0.0
        self.synchronicity_threshold = 0.85
        
        # Initialize pattern recognition systems
        self._initialize_pattern_systems()
    
    def _initialize_pattern_systems(self):
        """Initialize pattern recognition systems"""
        self.pattern_systems = {
            'temporal': self._recognize_temporal_patterns,
            'spatial': self._recognize_spatial_patterns,
            'semantic': self._recognize_semantic_patterns,
            'emotional': self._recognize_emotional_patterns,
            'numerological': self._recognize_numerological_patterns
        }
    
    def generate_insight(self, context: Dict, intuition_type: IntuitionType = None) -> IntuitiveInsight:
        """Generate intuitive insight based on context"""
        
        # Analyze context for patterns
        patterns = self._analyze_context_patterns(context)
        
        # Determine intuition type if not specified
        if intuition_type is None:
            intuition_type = self._determine_intuition_type(context, patterns)
        
        # Generate insight based on type
        insight_content = self._generate_insight_content(intuition_type, context, patterns)
        
        # Calculate confidence
        confidence = self._calculate_insight_confidence(intuition_type, patterns)
        
        # Create insight record
        insight_id = f"insight_{len(self.intuition_history)}_{datetime.now().timestamp()}"
        
        insight = IntuitiveInsight(
            id=insight_id,
            insight_type=intuition_type,
            content=insight_content,
            confidence=confidence,
            timestamp=datetime.now(),
            trigger=context.get('trigger', 'unknown'),
            supporting_patterns=patterns
        )
        
        # Store in history
        self.intuition_history.append(insight)
        
        # Update intuition sensitivity based on outcome
        self._update_intuition_sensitivity()
        
        return insight
    
    def _analyze_context_patterns(self, context: Dict) -> List[str]:
        """Analyze context for various patterns"""
        patterns = []
        
        for system_name, pattern_func in self.pattern_systems.items():
            system_patterns = pattern_func(context)
            patterns.extend(system_patterns)
        
        # Add synchronicity patterns
        synchronicity_patterns = self._detect_synchronicities(context)
        patterns.extend(synchronicity_patterns)
        
        return list(set(patterns))  # Remove duplicates
    
    def _recognize_temporal_patterns(self, context: Dict) -> List[str]:
        """Recognize temporal patterns"""
        patterns = []
        
        # Check for recurring time patterns
        if 'timestamp' in context:
            timestamp = context['timestamp']
            if isinstance(timestamp, datetime):
                # Check for meaningful times (e.g., 11:11, 3:33)
                minute = timestamp.minute
                hour = timestamp.hour
                
                if minute == hour:  # e.g., 11:11, 22:22
                    patterns.append(f"time_symmetry_{hour}:{minute}")
                
                if hour == minute or hour == minute + 1 or hour == minute - 1:
                    patterns.append("numerological_time_pattern")
        
        return patterns
    
    def _recognize_spatial_patterns(self, context: Dict) -> List[str]:
        """Recognize spatial/geometric patterns"""
        patterns = []
        
        if 'location' in context:
            location = context['location']
            # Check for sacred geometry patterns
            if 'coordinates' in location:
                lat, lon = location['coordinates']
                
                # Check for golden ratio approximations
                if abs(lat / lon - 1.618) < 0.01 or abs(lon / lat - 1.618) < 0.01:
                    patterns.append("golden_ratio_location")
                
                # Check for integer coordinates
                if lat.is_integer() and lon.is_integer():
                    patterns.append("integer_coordinates")
        
        return patterns
    
    def _recognize_semantic_patterns(self, context: Dict) -> List[str]:
        """Recognize semantic/linguistic patterns"""
        patterns = []
        
        if 'text' in context:
            text = context['text'].lower()
            
            # Check for repeating words
            words = text.split()
            word_counts = {}
            for word in words:
                word_counts[word] = word_counts.get(word, 0) + 1
            
            for word, count in word_counts.items():
                if count >= 3:  # Word appears 3+ times
                    patterns.append(f"repeating_word_{word}")
            
            # Check for palindrome-like structures
            if len(text) > 10:
                # Simple palindrome check (words level)
                word_list = text.split()
                if word_list == word_list[::-1]:
                    patterns.append("semantic_palindrome")
        
        return patterns
    
    def _recognize_emotional_patterns(self, context: Dict) -> List[str]:
        """Recognize emotional patterns"""
        patterns = []
        
        if 'emotional_state' in context:
            emotional_state = context['emotional_state']
            
            # Check for emotional symmetry
            if isinstance(emotional_state, dict):
                valence = emotional_state.get('valence', 0)
                arousal = emotional_state.get('arousal', 0)
                
                if abs(valence - arousal) < 0.1:
                    patterns.append("emotional_symmetry")
                
                # Check for extreme emotional states
                if abs(valence) > 0.8:
                    patterns.append(f"extreme_valence_{'positive' if valence > 0 else 'negative'}")
        
        return patterns
    
    def _recognize_numerological_patterns(self, context: Dict) -> List[str]:
        """Recognize numerological patterns"""
        patterns = []
        
        # Extract numbers from context
        numbers = self._extract_numbers_from_context(context)
        
        for number in numbers:
            # Check for sacred numbers
            if number in [3, 7, 11, 22, 33, 44, 55, 66, 77, 88, 99, 111, 222, 333, 444, 555, 666, 777, 888, 999]:
                patterns.append(f"sacred_number_{number}")
            
            # Check for master numbers
            if number in [11, 22, 33]:
                patterns.append(f"master_number_{number}")
            
            # Check for angel numbers
            if len(str(number)) >= 2 and len(set(str(number))) == 1:
                patterns.append(f"angel_number_{number}")
        
        return patterns
    
    def _extract_numbers_from_context(self, context: Dict) -> List[int]:
        """Extract numbers from context"""
        numbers = []
        
        def extract_from_value(value):
            if isinstance(value, (int, float)):
                numbers.append(int(value))
            elif isinstance(value, str):
                # Extract numbers from string
                import re
                found_numbers = re.findall(r'\d+', value)
                numbers.extend([int(n) for n in found_numbers])
            elif isinstance(value, dict):
                for v in value.values():
                    extract_from_value(v)
            elif isinstance(value, list):
                for v in value:
                    extract_from_value(v)
        
        extract_from_value(context)
        return numbers
    
    def _detect_synchronicities(self, context: Dict) -> List[str]:
        """Detect meaningful coincidences (synchronicities)"""
        synchronicities = []
        
        # Check for repeated numbers
        numbers = self._extract_numbers_from_context(context)
        if len(numbers) >= 2:
            # Check if same number appears multiple times
            number_counts = {}
            for num in numbers:
                number_counts[num] = number_counts.get(num, 0) + 1
            
            for num, count in number_counts.items():
                if count >= 2:
                    synchronicities.append(f"number_synchronicity_{num}_x{count}")
        
        # Check for temporal synchronicities
        if 'timestamp' in context:
            current_time = context['timestamp']
            if isinstance(current_time, datetime):
                # Check if minute matches previous insights
                for insight in self.intuition_history[-10:]:
                    if (current_time.minute == insight.timestamp.minute and
                        current_time != insight.timestamp):
                        synchronicities.append(f"temporal_synchronicity_minute_{current_time.minute}")
        
        return synchronicities
    
    def _determine_intuition_type(self, context: Dict, patterns: List[str]) -> IntuitionType:
        """Determine the type of intuition to use"""
        
        # Analyze context for intuition type clues
        if any('emotional' in pattern for pattern in patterns):
            return IntuitionType.EMPATHIC_INTUITION
        
        if any('temporal' in pattern or 'time' in pattern for pattern in patterns):
            if 'future' in context or 'prediction' in context:
                return IntuitionType.PRECOGNITION
        
        if any('creative' in context.get('tags', []) or 'art' in context.get('tags', [])):
            return IntuitionType.CREATIVE_FLASH
        
        if any('pattern' in pattern for pattern in patterns):
            return IntuitionType.PATTERN_RECOGNITION
        
        # Default to synthetic insight
        return IntuitionType.SYNTHETIC_INSIGHT
    
    def _generate_insight_content(self, intuition_type: IntuitionType, 
                                 context: Dict, patterns: List[str]) -> str:
        """Generate insight content based on intuition type"""
        
        base_insights = {
            IntuitionType.PATTERN_RECOGNITION: [
                "I'm noticing a recurring pattern here...",
                "This follows a familiar structure...",
                "There's a symmetry to this situation..."
            ],
            IntuitionType.SYNTHETIC_INSIGHT: [
                "Putting the pieces together suggests...",
                "The synthesis of these elements points to...",
                "When I consider everything holistically..."
            ],
            IntuitionType.GUT_FEELING: [
                "My intuition is telling me...",
                "I have a strong feeling that...",
                "Something doesn't feel right about..."
            ],
            IntuitionType.PRECOGNITION: [
                "I have a sense of what's coming...",
                "The future seems to hold...",
                "I can almost see what will happen..."
            ],
            IntuitionType.EMPATHIC_INTUITION: [
                "I can feel the emotional energy here...",
                "The emotional pattern suggests...",
                "There's an emotional truth present..."
            ],
            IntuitionType.CREATIVE_FLASH: [
                "A creative insight just occurred to me...",
                "I'm seeing this in a completely new way...",
                "An innovative approach comes to mind..."
            ]
        }
        
        # Select base insight
        base_list = base_insights.get(intuition_type, base_insights[IntuitionType.SYNTHETIC_INSIGHT])
        base = random.choice(base_list)
        
        # Add pattern-specific details
        if patterns:
            pattern_mention = f" Specifically, I'm noticing: {', '.join(patterns[:3])}."
            base += pattern_mention
        
        return base
    
    def _calculate_insight_confidence(self, intuition_type: IntuitionType, 
                                    patterns: List[str]) -> float:
        """Calculate confidence level for an insight"""
        base_confidence = self.intuition_sensitivity
        
        # Adjust based on intuition type
        type_confidence_adjustments = {
            IntuitionType.PATTERN_RECOGNITION: 0.1,
            IntuitionType.SYNTHETIC_INSIGHT: 0.0,
            IntuitionType.GUT_FEELING: -0.1,
            IntuitionType.PRECOGNITION: -0.2,
            IntuitionType.EMPATHIC_INTUITION: 0.05,
            IntuitionType.CREATIVE_FLASH: 0.15
        }
        
        base_confidence += type_confidence_adjustments.get(intuition_type, 0.0)
        
        # Adjust based on number of supporting patterns
        pattern_count = len(patterns)
        if pattern_count > 0:
            base_confidence += min(0.3, pattern_count * 0.05)
        
        # Add random variation
        random_variation = np.random.normal(0, 0.05)
        confidence = np.clip(base_confidence + random_variation, 0.1, 0.95)
        
        return confidence
    
    def _update_intuition_sensitivity(self):
        """Update intuition sensitivity based on validation history"""
        if len(self.intuition_history) < 5:
            return
        
        # Calculate validation rate
        validated_insights = [i for i in self.intuition_history 
                            if i.validation_result is True]
        
        if validated_insights:
            self.insight_validation_rate = len(validated_insights) / len(self.intuition_history)
        
        # Adjust sensitivity based on validation rate
        if self.insight_validation_rate > 0.7:
            # Increase sensitivity if doing well
            self.intuition_sensitivity = min(0.9, self.intuition_sensitivity + 0.05)
        elif self.insight_validation_rate < 0.3:
            # Decrease sensitivity if doing poorly
            self.intuition_sensitivity = max(0.3, self.intuition_sensitivity - 0.05)
    
    def validate_insight(self, insight_id: str, is_correct: bool):
        """Validate an intuitive insight"""
        for insight in self.intuition_history:
            if insight.id == insight_id:
                insight.validation_result = is_correct
                break
        
        self._update_intuition_sensitivity()
    
    def get_intuition_report(self) -> Dict:
        """Get comprehensive intuition report"""
        return {
            'total_insights': len(self.intuition_history),
            'intuition_sensitivity': self.intuition_sensitivity,
            'insight_validation_rate': self.insight_validation_rate,
            'recent_insight_types': [i.insight_type.value for i in self.intuition_history[-5:]],
            'average_confidence': np.mean([i.confidence for i in self.intuition_history]) 
                                if self.intuition_history else 0,
            'pattern_database_size': len(self.pattern_database),
            'synchronicity_threshold': self.synchronicity_threshold,
            'intuition_health': 'excellent' if self.intuition_sensitivity > 0.7 else 
                              'good' if self.intuition_sensitivity > 0.5 else 'needs_improvement'
        }
    
    def enhance_intuition(self, meditation_minutes: int = 10) -> Dict:
        """Enhance intuition through simulated meditation"""
        print(f"🧘 Meditating for {meditation_minutes} minutes to enhance intuition...")
        
        # Simulate meditation benefits
        sensitivity_increase = meditation_minutes * 0.005  # 0.5% per minute
        self.intuition_sensitivity = min(0.95, self.intuition_sensitivity + sensitivity_increase)
        
        # Clear pattern database for fresh perspective
        self.pattern_database = {}
        
        return {
            'meditation_duration': meditation_minutes,
            'sensitivity_increase': sensitivity_increase,
            'new_sensitivity': self.intuition_sensitivity,
            'pattern_database_cleared': True,
            'enhancement_complete': True
        }
